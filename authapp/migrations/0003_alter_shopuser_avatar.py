# Generated by Django 3.2.10 on 2022-01-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20220105_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default_profile_photo.png', upload_to='avatar', verbose_name='Фото профиля'),
        ),
    ]
