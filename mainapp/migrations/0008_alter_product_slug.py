# Generated by Django 3.2.10 on 2022-01-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0007_auto_20220102_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=70, unique=True),
        ),
    ]
