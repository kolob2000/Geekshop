import json

from django.shortcuts import render


# Create your views here.


def main(request):
    # title = 'главная'
    # products = [
    #     {
    #         'img': 'img/product-1.jpg',
    #         'icon': 'img/icon-hover.png',
    #         'title': 'Отличный стул',
    #         'text': 'Расположитесь комфортно',
    #     },
    #     {
    #         'img': 'img/product-2.jpg',
    #         'icon': 'img/icon-hover.png',
    #         'title': 'Стул повышенного качества',
    #         'text': 'Не оторваться',
    #     },
    # ]
    # context = {
    #     'title': title,
    #     'products': products,
    # }
    with open('mainapp/main.json', 'r') as f:
        context = json.loads(f.read())
    print(context)
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    # title = 'продукты'
    #
    # menu_links = [
    #     {'href': 'products', 'name': 'Все'},
    #     {'href': 'house', 'name': 'Дом'},
    #     {'href': 'office', 'name': 'Офис'},
    #     {'href': 'modern', 'name': 'Модерн'},
    #     {'href': 'classic', 'name': 'Классика'},
    # ]
    # slider_product = [
    #     {'img': 'img/controll.jpg', },
    #     {'img': 'img/controll1.jpg', },
    #     {'img': 'img/controll2.jpg', },
    # ]
    # rel_products = [
    #     {
    #         'img': 'img/product-11.jpg',
    #         'icon': 'img/icon-hover.png',
    #         'title': 'Люстра повышенного качества',
    #         'text': 'Не оторваться',
    #     },
    #     {
    #         'img': 'img/product-21.jpg',
    #         'icon': 'img/icon-hover.png',
    #         'title': 'Стул повышенного качества',
    #         'text': 'Не оторваться',
    #     },
    #     {
    #         'img': 'img/product-31.jpg',
    #         'icon': 'img/icon-hover.png',
    #         'title': 'Торшер повышенного качества',
    #         'text': 'Не оторваться',
    #     },
    # ]
    # context = {
    #     'menu_links': menu_links,
    #     'title': title,
    #     'slider_product': slider_product,
    #     'rel_products': rel_products,
    # }
    with open('mainapp/products.json', 'r') as f:
        context = json.loads(f.read())
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    # title = 'контакты и т.д.'
    # contacts = [
    #     {
    #         'city': 'Петропавловск-Камчатский',
    #         'phone': '+7-888-888-8888',
    #         'email': 'info@geekshop.ru',
    #         'address': 'ул. Труда 33',
    #     },
    #     {
    #         'city': 'Санкт-Петербург',
    #         'phone': '+7-888-888-8888',
    #         'email': 'info@geekshop.ru',
    #         'address': 'ул. Русановская',
    #     },
    #     {
    #         'city': 'Барнаул',
    #         'phone': '+7-888-888-8888',
    #         'email': 'info@geekshop.ru',
    #         'address': 'ул. Ленина',
    #     },
    #
    # ]
    # context = {
    #     'title': title,
    #     'contacts': contacts
    # }
    with open('mainapp/contact.json', 'r') as f:
        context = json.loads(f.read())
    return render(request, 'mainapp/contact.html', context=context)
