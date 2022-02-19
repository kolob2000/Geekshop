from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from basket.models import Basket
from orderapp.forms import OrderItemForm
from orderapp.models import Order, OrderItem


class OrdersListView(ListView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrdersListView, self).get_context_data(**kwargs)
        context['title'] = 'Мои заказы'
        return context

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreateView(CreateView):
    model = Basket


class OrderItemDetailView(DetailView):
    pass


class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('orderapp:edit_order', args=(self.object.order_id,))


class OrderItemDeleteView(DeleteView):
    model = OrderItem

    def get_success_url(self, **kwargs):
        order = Order.objects.get(pk=self.object.order_id)
        if order.get_total_qunatity2 - self.object.quantity > 0:
            return reverse_lazy('orderapp:edit_order', args=(self.object.order_id,))
        else:
            order = Order.objects.filter(pk=self.object.order_id)
            order.delete()
            return reverse_lazy('order:orders_list')


@transaction.atomic
def add_order(request, val):
    if val:
        basket = Basket.objects.filter(user=request.user)
        order = Order.objects.create(user=request.user)
        for item in basket:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            item.delete()

        return HttpResponseRedirect(reverse('order:orders_list'))
    else:
        return render(request, 'orderapp/order_confirm.html', context={'val': 1, 'title': 'Подтверждение заказа'})


@transaction.atomic
def delete_order(request, pk):
    order_items = OrderItem.objects.filter(order_id=pk)
    order_items.delete()
    cur_order = Order.objects.filter(pk=pk)
    cur_order.delete()
    return HttpResponseRedirect(reverse('order:orders_list'))


@transaction.atomic
def edit_order(request, pk):
    context = {
        'order_items': OrderItem.objects.filter(order_id=pk),
        'title': f'Изменить заказ 005{pk}',
    }
    return render(request, 'orderapp/edit_order.html', context=context)
