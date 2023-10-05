from django.contrib import admin
from order.models import *

# Register your models here.
admin.site.register(Payments)
admin.site.register(Order)
admin.site.register(OrderProduct)