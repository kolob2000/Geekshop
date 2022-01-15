from django.db.models import Sum

from .models import Basket


def quantity(request):
    if str(request.user) == 'AnonymousUser':
        return {'basket_quantity': False}
    count = Basket.objects.all().filter(user=request.user).aggregate(Sum('quantity'))
    return {'basket_quantity': count['quantity__sum']}
