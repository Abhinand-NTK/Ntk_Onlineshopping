"""Clothselling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
        path('addtocart/<int:product_vareint_id>',views.Add_to_Cart,name='addtocart'),
        path('cart_item/',views.Cart_page,name='cart_item'),
        path('delete_from_cart/<str:delete_id>',views.Cart_delete,name='delete_from_cart'),
        path('check_out/',views.Checkout,name='check_out'),
        path('cart_item/update_quantity/',views.update_cart_item_quantity,name='update_quantity'),

]
