# Generated by Django 3.2.10 on 2022-01-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Эл. почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, unique=True, verbose_name='Телефон'),
        ),
    ]
