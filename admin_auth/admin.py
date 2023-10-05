from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductVariant) 
admin.site.register(Product)
admin.site.register(Subcategory)
admin.site.register(Coupons)
admin.site.register(Banner)
admin.site.register(Brand)
admin.site.register(Multipleimges)
admin.site.register(Rating)
