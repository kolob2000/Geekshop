from django.urls import re_path
import basket.views as basket

app_name = 'basket'
urlpatterns = [
    re_path(r'^$', basket.view, name='basket'),
    re_path(r'^add/(?P<pk>\d+)/$', basket.add, name='add'),
    re_path(r'^edit/$', basket.edit, name='edit'),
    re_path(r'^remove/$', basket.remove, name='remove'),

]
