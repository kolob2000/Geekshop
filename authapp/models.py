from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta

# Create your models here.
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, verbose_name='Фото профиля',
                               default='avatar/default_profile_photo.png')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=25)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    REQUIRED_FIELDS = ('age', 'email',)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
