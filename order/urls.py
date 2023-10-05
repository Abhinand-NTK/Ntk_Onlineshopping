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
        path('placeorder/',views.Place_Order,name='placeorder'),
        path('placeorder_online/',views.Place_Order_online_Payment,name='placeorder_online'),

        path('remove-show-modal/', views.remove_show_modal_session, name='remove_show_modal_session'),
        path('order_details/<int:order_id>/', views.Order_deatails, name='order_details'),

        path('returnorder/<int:order_id>/', views.Returntheorder, name='returnorder'),
        path('cancelorder/<int:order_id>/', views.Cancelorder, name='cancelorder'),
        path('returnindivudal/<int:id>/', views.Cancel_indivdal_items, name='returnindivudal'),
        path('returnindivudalproducts/<int:itemid>', views.Refunded_for_indivdal_items, name='returnindivudalproducts'),

        path('get-address-details/', views.get_address_details, name='get_address_details'),
        path('proceed-to-pay/', views.razorpaycheck, name='proceed-to-pay'),


]
