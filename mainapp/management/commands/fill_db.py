import json

from django.core.management import BaseCommand

from mainapp.models import Category, Product


def json_to_dict(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = json_to_dict('mainapp/json/categories.json')
        for i in categories:
            cat = Category(**i)
            cat.save()
        products = json_to_dict('mainapp/json/products.json')
        for i in products:
            i['category'] = Category.objects.get(pk=i['category'])
            product = Product(**i)
            product.save()
        print('data was loaded.')
