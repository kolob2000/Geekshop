from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.main, name='index'),
    path('user_create/', adminapp.user_create, name='user_create'),
    path('user_update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user_delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    ################################################################
    path('categoreis/create/', adminapp.category_update, name='category_create'),
    path('categoreis/', adminapp.category_read, name='category_read'),
    path('categoreis/update/<int:pk>/', adminapp.category_update, name='category_update'),
    # path('categoreis/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categoreis/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),
    #################################################################
    path('category/poducts/<int:pk>/', adminapp.product_read, name='product_read'),
    path('product/create/<int:pk>/', adminapp.product_create, name='product_create'),
    path('product/<int:pk>/', adminapp.product_update, name='product_update'),
    path('product/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

]
