from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, verbose_name='Фото профиля',
                               default='avatar/default_profile_photo.png')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    REQUIRED_FIELDS = ('age', 'email',)
