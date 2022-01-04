from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from pytils import translit


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание', default='Здесь должно быть описание...')
    slug = models.SlugField(max_length=70, unique=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(blank=True, upload_to='media', )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Старая цена')
    description = models.TextField(default='Описание товара...', verbose_name='Описание', blank=True)
    short_desc = models.CharField(max_length=255, blank=True, default='Короткое описание',
                                  verbose_name='Короткое описание')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    is_stock = models.BooleanField(default=True, verbose_name='На складе')
    slug = models.SlugField(max_length=70, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        if sender.objects.count():
            instance.slug = translit.slugify(instance.title + '-' + str(sender.objects.order_by('-pk')[0].pk + 1))
        else:
            instance.slug = translit.slugify(instance.title + '-' + '1')


pre_save.connect(slug_generator, sender=Product)
pre_save.connect(slug_generator, sender=Category)


class ImageGallery(models.Model):
    image = models.ImageField(blank=True, upload_to='media')
    product = models.ForeignKey(Product, default=None, blank=True, related_name='images', on_delete=models.PROTECT)


class Contact(models.Model):
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='Эл. почта')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.city
