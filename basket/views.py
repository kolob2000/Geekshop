from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Basket, Product


# Create your views here.
def view(request):
    return None


def add(request, pk):
    basket = Basket.objects.filter(user=request.user, product_id=pk).first()
    if basket:
        basket.quantity += 1
        basket.save()
    else:
        product = get_object_or_404(Product, pk=pk)
        Basket.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(reverse('main'))
