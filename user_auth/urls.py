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
    path('',views.User_login,name='user_login'),
    path('logout/',views.User_logout,name='user_logout'),

    path('signup/',views.User_signup,name='user_signup'),
    path('Validation/',views.Signupvalidation,name='validation'),
    path('addprofilepicture/<int:user_id>',views.Addpropic,name='addprofilepicture'),
    path('myprofile/',views.Myprofile,name='myprofile'),
    path('myprofile_edit/',views.Edit_profile,name='myprofile_edit'),


    path('forgetpas/',views.User_forgetpassword,name='forget_password'),
    path('otpverifiaction/<int:user_id>',views.User_otpverification,name='otp_verification'),
    path('resetpas/<int:user_id>',views.User_resetpassword,name='reset_password'),


    

    path('manageadress/',views.Manage_Address,name='manageadress'),
    path('manageadress_edit/<int:adress_id>',views.Manage_Edit_Address,name='manageadress_edit'),
    path('manageadress_delete/<int:adress_id>',views.Manage_Address_delete,name='manageadress_delete'),

    
    path('myorder/',views.Myorder,name='myorder'),
    path('coupenslist/',views.Coupenlist,name='coupenslist'),
    path('mywallet/',views.Mywallet,name='mywallet'),
    path('mywishlist/<int:varient_id>',views.Mywishlist,name='mywishlist'),
    path('deletewish/<int:delete_id>',views.Delete_wish,name='deletewish'),
    path('addtocartfromwishlist/<int:product_vareint_id>',views.Add_item_to_Cart,name='addtocartfromwishlist'),
    path('rating/<int:variant_id>', views.Submit_rating, name='submit_rating'),
    path('printinvoice/<int:order_id>',views.Print_invoice,name='printinvoice'),

    


]
