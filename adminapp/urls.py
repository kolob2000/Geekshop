from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main, name='index'),
    re_path(r'^user_create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user_update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user_delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    ################################################################
    re_path(r'^categoreis/create/$', adminapp.category_update, name='category_create'),
    re_path(r'^categoreis/$', adminapp.category_read, name='category_read'),
    re_path(r'^categoreis/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    re_path('categoreis/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    # re_path(r'^categoreis/delete/(?P<pk>\d+)/$', adminapp.CategoryDeleteView.as_view(), name='category_delete'),
    #################################################################
    re_path(r'^category/poducts/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    re_path(r'^product/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^product/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),

]
