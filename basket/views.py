from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Basket, Product


# Create your views here.
@login_required
def view(request):
    context = {
        'title': 'Корзина',
        'basket': Basket.objects.all().filter(user=request.user),
    }
    return render(request, 'basketapp/basket.html', context=context)


def add(request, pk):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('auth:login'))
    basket = Basket.objects.filter(user=request.user, product_id=pk).first()
    if basket:
        basket.quantity += 1
        basket.save()
    else:
        product = get_object_or_404(Product, pk=pk)
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit(request):
    pk = int(request.GET['pkey'])
    quantity = int(request.GET['quantity'])

    product = get_object_or_404(Basket, pk=pk)
    if quantity:
        product.quantity = quantity
        product.save()
    else:
        product.delete()
    context = {
        'basket': Basket.objects.all().filter(user=request.user),
    }
    return render(request, 'basketapp/basket_ajax.html', context=context)


def remove(request):
    pk = int(request.GET['pkey'])
    product = get_object_or_404(Basket, pk=pk)
    product.delete()
    context = {
        'basket': Basket.objects.all().filter(user=request.user)
    }
    return render(request, 'basketapp/basket_ajax.html', context=context)
