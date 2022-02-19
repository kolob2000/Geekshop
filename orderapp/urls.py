from django.urls import re_path, path
import orderapp.views as order

app_name = 'orderapp'
urlpatterns = [
    re_path(r'^$', order.OrdersListView.as_view(), name='orders'),
    re_path(r'^user_orders/$', order.OrdersListView.as_view(), name='orders_list'),
    path('add_order/<int:val>/', order.add_order, name='add_order'),
    path('delete_order/<int:pk>/', order.delete_order, name='delete_order'),
    path('edit_order/<int:pk>/', order.edit_order, name='edit_order'),
    # re_path(r'^add_order/(?P<int>\d+)/$', order.add_order, name='add_order'),
    re_path(r'^create/(?P<pk>\d+)/$', order.OrderCreateView.as_view(), name='create'),
    re_path(r'^read/(?P<pk>\d+)/$', order.OrderItemDetailView.as_view(), name='read'),
    re_path(r'^update/(?P<pk>\d+)/$', order.OrderItemUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', order.OrderItemDeleteView.as_view(), name='delete'),

]
