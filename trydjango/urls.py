"""trydjango URL Configuration

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
from django.contrib import admin
from django.urls import path

from carts.views import cart_detail_view,cart_create_view,search

urlpatterns = [

    path('admin/', admin.site.urls),
path('cart', cart_detail_view, name='cart_d'),
    path('paranjolu',cart_create_view,name='cart_c'),
path('kettolu',cart_detail_view,name='kettolu'),
path('search',search,name='search'),
]
