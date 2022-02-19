from django.db import models

from geekshop import settings
from mainapp.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    add_at = models.DateTimeField(auto_now_add=True, verbose_name='время добавления')

    @property
    def product_cost(self):
        return self.quantity * self.product.price
