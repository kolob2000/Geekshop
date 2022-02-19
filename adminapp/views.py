from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin

from adminapp.forms import ShopUserAdminChangeForm, CategoryEditForm, ProductEditForm
from authapp.models import ShopUser
from authapp.forms import ShopUserCreationForm
from mainapp.models import Category, Product
from orderapp.forms import OrderItemForm, OrderForm
from orderapp.models import Order, OrderItem


@user_passes_test(lambda user: user.is_superuser)
def main(request):
    context = {
        'title': 'Администрирование',
        'users': ShopUser.objects.all()
    }
    return render(request, 'adminapp/index.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = ShopUserCreationForm
    context = {
        'title': 'Создать пользователя',
        'form': form,
    }
    return render(request, 'adminapp/user_create.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminChangeForm(request.POST, request.FILES, instance=edit_user)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = ShopUserAdminChangeForm(instance=edit_user)
    context = {
        'title': 'Изменить данные',
        'form': form,
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user = ShopUser.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return render(request, 'adminapp/includes/ajax-users.html', context={'users': ShopUser.objects.all(), })


@user_passes_test(lambda user: user.is_superuser)
def category_read(request):
    context = {
        'categories': Category.objects.all(),
        'title': 'Категории',
    }
    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def category_update(request, pk=None):
    if pk:
        edit_category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            form = CategoryEditForm(request.POST, instance=edit_category)
            if form.is_valid():
                form.save()
                return redirect('admin:category_read')
        else:
            form = CategoryEditForm(instance=edit_category)
    else:
        if request.method == 'POST':
            new_category = CategoryEditForm(request.POST)
            if new_category.is_valid():
                new_category.save()
                return redirect('admin:category_read')
        else:
            form = CategoryEditForm()
    context = {
        'title': 'Редактировать категорию',
        'form': form,
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category.is_active:
        category.is_active = False
    else:
        category.is_active = True
    category.save()
    return render(request, 'adminapp/includes/ajax-category.html', context={'categories': Category.objects.all(), })


# class CategoryDeleteView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         category = Category.objects.get(pk=kwargs['pk'])
#         if category.is_active:
#             category.is_active = False
#         else:
#             category.is_active = True
#         category.save()
#         return render(self.request, 'adminapp/includes/ajax-category.html',
#                       context={'categories': Category.objects.all(), })


def product_read(request, pk):
    category = get_object_or_404(Category, pk=pk)
    objects = category.product_set.all()
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {
        'title': category.title,
        'products': page_objects,
    }
    return render(request, 'adminapp/products_by_category.html', context=context)


# def product_read(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     context = {
#         'title': category.title,
#         'products': category.product_set.all(),
#     }
#     return render(request, 'adminapp/products_by_category.html', context=context)


def product_create(request, pk):
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:product_read', args=[pk]))
    category = get_object_or_404(Category, pk=pk)
    context = {
        'title': 'Создать продукт',
        'form': ProductEditForm(initial={'category': category}),
    }
    return render(request, 'adminapp/product_create.html', context=context)


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category.pk
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:product_read', args=[category]))
    else:
        context = {
            'title': 'Редактировать продукт',
            'form': ProductEditForm(instance=product)
        }
    return render(request, 'adminapp/product_update.html', context=context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = product.category.pk
    if product.is_active:
        product.is_active = False
    else:
        product.is_active = True
    product.save()
    return HttpResponseRedirect(reverse('admin:product_read', args=[category]))


class OrdersListView(ListView):
    model = Order
    template_name = 'adminapp/order_list.html'


class OrderUpdateView(UpdateView):
    model = Order
    fields = []
    template_name = 'adminapp/order_update_forms.html'

    def get_success_url(self):
        with transaction.atomic():
            order = Order.objects.get(pk=self.object.id)
            if order.get_total_qunatity2 == 0:
                order = Order.objects.filter(pk=self.object.id)
                order.delete()
        return reverse_lazy('adminapp:order_list')

    def get_context_data(self, **kwargs):
        data = super(OrderUpdateView, self).get_context_data(**kwargs)
        data['title'] = 'Изменить заказ'
        OrderFormSet = inlineformset_factory(Order, OrderItem, OrderItemForm, extra=1)
        if self.request.POST:
            data['orderitems'] = OrderFormSet(self.request.POST, instance=self.object)
        else:
            data['orderitems'] = OrderFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderUpdateView, self).form_valid(form)


class OrderCreateView(CreateView):
    model = Order
    fields = ('user', 'status',)
    template_name = 'adminapp/order_form.html'

    def get_form(self, form_class=None):
        form = super(OrderCreateView, self).get_form(form_class=form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_success_url(self):
        return reverse_lazy('adminapp:order_update', args=(self.object.id,))
