from django.urls import re_path, path

import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    # re_path('', mainapp.products, name='products'),
    re_path(r'^$', mainapp.ProductListView.as_view(), kwargs={'slug': None}, name='products'),
    re_path(r'^(?P<slug>[\w-]+)/$', mainapp.ProductListView.as_view(), name='category'),
    re_path(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', mainapp.ProductDetailView.as_view(), name='product')

]
