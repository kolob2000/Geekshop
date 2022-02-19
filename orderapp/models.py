from django.db import models

from geekshop import settings
from mainapp.models import Product


# Create your models here.


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNL'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'в обработке'),
        (PROCEEDED, 'обрабатывается'),
        (PAID, 'оплачен'),
        (READY, 'готов'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлен')
    status = models.CharField(max_length=3, verbose_name='статус', choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(default=True, verbose_name='активен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    def get_total_qunatity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    @property
    def get_total_qunatity2(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_qunatity(self):
        return len(self.orderitems.select_related())

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def delete(self):
        items = self.orderitems.select_related()
        for item in items:
            item.product.quantity = item.quantity
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity
