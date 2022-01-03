from django.shortcuts import render

from .models import Product, Category, Contact


def main(request):
    title = 'главная'
    context = {
        'title': title,
        'products': Product.objects.all().order_by('?')[:4],
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request, slug=None):
    title = 'продукты'
    context = {
        'menu_links': Category.objects.all(),
        'products': Product.objects.all(),
        'title': title,
        'rel_products': Product.objects.all().order_by('?')[:3],
    }

    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    title = 'контакты и т.д.'
    context = {
        'title': title,
        'contacts': Contact.objects.all()
    }

    return render(request, 'mainapp/contact.html', context=context)


def product_detail(request, category, product):
    product = Product.objects.get(slug=product)
    context = {
        'title': product.title,
        'product': product,
        'menu_links': Category.objects.all(),
        'rel_products': Product.objects.all().order_by('?')[:3],
    }
    return render(request, 'mainapp/product_detail.html', context=context)
