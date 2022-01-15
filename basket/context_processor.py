from django.db.models import Sum

from .models import Basket


def quantity(request):
    count = Basket.objects.all().aggregate(Sum('quantity'))
    return {'basket_quantity': count['quantity__sum']}
