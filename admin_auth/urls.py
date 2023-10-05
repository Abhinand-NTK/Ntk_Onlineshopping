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
from django.urls import path
from .import views
from django.conf.urls import handler404

handler404 = 'admin_auth.views.custom_404'




urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('logout/',views.logout_admin,name='logout'),

    path('dashboard/',views.admindashboard,name='admindashboard'),

    path('users/',views.adminusers,name='adminusers'),
    path('list_unlist_user/',views.admin_user_list_unlist,name='list_unlist_user'),

    path('products/',views.adminproducts,name='adminproducts'),
    path('products_list_unlist/',views.list_unlist_products,name='list_unlist_products'),
    path('category/',views.admincategory,name='category'),

    path('list_unlist_sub/',views.listsubcategory,name='list_unlist_subcategory'),
    path('list_unlist_cate/',views.listcategory,name='list_unlist_category'),

    path('addcategory/',views.addcategory,name='addcategory'),
    path('editcategory/<str:id>',views.editcategory,name='editcategory'),

    path('addsubcategory/',views.addsubcategory,name='addsubcategory'), 
    path('editsubcategory/<str:id>',views.editsubcategory,name='editcategory'),


    path('addcolorsize/',views.addcolor_size,name='addcolorsize'),  
    path('editcolorsize/<str:id>',views.edit_color_size,name='editcolorsize'),  


    path('addproducts',views.adminaddproducts,name='addproducts'),  
    path('editproducts/<str:id>',views.admineditproducts,name='editproducts'),  

    path('productvarients/', views.adminproductsvarients, name='productvarients'),
    path('editproductvarients/<str:id>', views.admineditproductsvarients, name='productvarients'),
    path('productvarientdetails/<int:id>', views.Productvarientdetails, name='productvarientdetails'),
    path('list_unlist_productvarient/', views.list_unlist_products_vareints, name='list_unlist_productvarient'),

    path('coupen_management/', views.Coupen_Management, name='coupen_management'),
    path('coupen_management_edit/<int:edit_coupen_id>', views.Coupen_Management_Edit, name='coupen_management_edit'),
    path('coupen/', views.Coupen, name='coupen'),

    path('ordermanagement/', views.Order_Management, name='ordermanagement'),
    path('orderdetailsmanagement/<int:manageorder_id>', views.Orderdetailsmanagement, name='orderdetailsmanagement'),
    path('orderstatus/<int:order_id>', views.Updatetheoderstatus, name='orderstatus'),


    path('generate_sales_report_pdf/', views.Admin_Sales_Report, name='generate_sales_report_pdf'),


    path('bannermanagement/', views.Banner_Management, name='bannermanagement'),
    path('delete_banner/<int:delete_id>', views.Delete_banner, name='delete_banner'),
    path('edit_banner/<int:edit_id>', views.Edit_banner, name='edit_banner'),



    path('totalorders/', views.Dashboard, name='totalorders'),



]



   


