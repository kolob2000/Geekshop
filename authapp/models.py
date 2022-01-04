from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, verbose_name='profile photo')
    age = models.PositiveIntegerField(verbose_name='age')
    REQUIRED_FIELDS = ('age', 'email',)
