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

urlpatterns=[
    path('',views.home,name='home'),
    path('category_selection/',views.product_category,name='category_selection'),
    path('womans/',views.Womans,name='womans'),
    path('mens/',views.Mens,name='mens'),
    path('kids/',views.kids,name='kids'),
    path('combos/',views.combos,name='combos'),
    path('products_details/<int:id>',views.product_details,name='details'),
    path('filtering_varient/', views.Filtering_in_Prouduct_details_page, name='filtering_varient'),
    path('filter/<str:category_id>/<str:heading>', views.Filter, name='filter'),
    path('multiple_filter/<str:heading>', views.filter_Accordence_multiple_input, name='multiple_filter'),
    path('search_products/<str:query>', views.search_products, name='search_products'),


    # path('filtering_varient/<str:varient_id>',views.product_details,name='filtering_varient'),
      ]

