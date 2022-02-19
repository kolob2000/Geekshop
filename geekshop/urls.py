"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

import geekshop.view
import mainapp.views as mainapp
from django.conf import settings

# from mainapp.models import Category


urlpatterns = [
    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    re_path(r'^$', mainapp.MainListView.as_view(), name='main'),
    # path('', mainapp.main, name='main'),
    re_path(r"^products/", include("mainapp.urls", namespace="products")),
    re_path(r"^auth/", include("authapp.urls", namespace="auth")),
    re_path(r"^basket/", include("basket.urls", namespace="basket")),
    re_path(r"^order/", include("orderapp.urls", namespace="order")),
    re_path(r'^contact/', mainapp.ContactListView.as_view(), name='contact'),
    re_path(r'^social/', include('social_django.urls', namespace='social')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'geekshop.view.page_not_found_view'
