# Generated by Django 3.2.10 on 2022-01-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0010_category_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
    ]
