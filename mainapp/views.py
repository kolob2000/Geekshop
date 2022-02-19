from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Category, Contact


class MainListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        context['title'] = 'главная'
        return context

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:4]


# def main(request):
#     title = 'главная'
#     context = {
#         'title': title,
#         'products': Product.objects.all().order_by('?')[:4],
#     }
#     return render(request, 'mainapp/index.html', context=context)

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/products.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Продукты'
        context['menu_links'] = Category.objects.all().filter(is_active=True)
        context['rel_products'] = Product.objects.all().filter(is_active=True).order_by('?')[:3] if self.kwargs[
                                                                                                        'slug'] is None else Category.objects.get(
            slug=self.kwargs['slug']).product_set.all().filter(is_active=True).order_by('?')[:3]
        return context

    def get_queryset(self):
        return Product.objects.all().filter(is_active=True) if self.kwargs['slug'] is None else Category.objects.get(
            slug=self.kwargs['slug']).product_set.all().filter(is_active=True)


# def products(request, slug=None):
#     title = 'продукты'
#     context = {
#         'menu_links': Category.objects.all(),
#         'products': Product.objects.all() if slug is None else Category.objects.get(slug=slug).product_set.all(),
#         'title': title,
#         'rel_products': Product.objects.all().order_by('?')[:3] if slug is None else Category.objects.get(
#             slug=slug).product_set.all().order_by('?')[:3],
#     }
#
#     return render(request, 'mainapp/products.html', context=context)
class ContactListView(ListView):
    model = Contact
    template_name = 'mainapp/contact.html'
    extra_context = {'title': 'Контакты'}
    context_object_name = 'contacts'


# def contact(request):
#     title = 'контакты и т.д.'
#     context = {
#         'title': title,
#         'contacts': Contact.objects.all()
#     }
#
#     return render(request, 'mainapp/contact.html', context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = context['product'].title
        context['menu_links'] = Category.objects.all()
        context['rel_products'] = Product.objects.all().order_by('?')[:3]
        return context

# def product_detail(request, category, product):
#     product = Product.objects.get(slug=product)
#     context = {
#         'title': product.title,
#         'product': product,
#         'menu_links': Category.objects.all(),
#         'rel_products': Product.objects.all().order_by('?')[:3],
#     }
#     return render(request, 'mainapp/product_detail.html', context=context)
