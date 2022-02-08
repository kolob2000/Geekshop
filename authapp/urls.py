from django.urls import re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login, name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^register/$', authapp.register, name='register'),
    re_path(r'^user_edit/$', authapp.user_edit, name='user_edit'),
    re_path(r'^user_profile/$', authapp.user_profile, name='user_profile'),
    re_path(r'^verify/(?P<email>.+)/(?P<key>\w+)/$', authapp.verify, name='verify'),
]
