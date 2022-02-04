from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    # path('', mainapp.products, name='products'),
    path('', mainapp.ProductListView.as_view(), kwargs={'slug': None}, name='products'),
    path('<slug:slug>/', mainapp.ProductListView.as_view(), name='category'),
    path('<slug:category_slug>/<slug:slug>/', mainapp.ProductDetailView.as_view(), name='product')
]
