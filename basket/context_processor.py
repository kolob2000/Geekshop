from django.db.models import Sum

from .models import Basket


def quantity(request):
    if request.user.is_anonymous:
        return {'basket_quantity': False}
    count = Basket.objects.all().filter(user=request.user).aggregate(Sum('quantity'))
    return {'basket_quantity': count['quantity__sum']}


def total_cost(request):
    if request.user.is_anonymous:
        return {'basket_cost': False}
    basket = Basket.objects.all().filter(user=request.user)
    return {'basket_cost': sum(map(lambda x: x.product.price * x.quantity, basket))}
