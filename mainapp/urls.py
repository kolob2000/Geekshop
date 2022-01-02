from django.urls import path

# import views as mainapp
import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<slug:slug>/', mainapp.products, name='category'),
    path('<slug:category>/<slug:product>/', mainapp.product_detail, name='product')
]

