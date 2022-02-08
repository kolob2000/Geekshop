from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, verbose_name='Фото профиля',
                               default='avatar/default_profile_photo.png')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=25)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    REQUIRED_FIELDS = ('age', 'email',)

    class Meta:
        unique_together = ('email',)
        verbose_name = 'Пользователь'

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    ]
    user = models.OneToOneField(ShopUser, unique=True, on_delete=models.CASCADE, db_index=True)
    gender = models.CharField(max_length=1, verbose_name='пол', blank=True, choices=GENDER)
    hash_tags = models.CharField(max_length=255, verbose_name='хэштеги', blank=True)
    about_me = models.TextField(verbose_name='обо мне', blank=True)


@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)


@receiver(post_save, sender=ShopUser)
def save_user_profile(sender, instance, **kwargs):
    instance.shopuserprofile.save()
