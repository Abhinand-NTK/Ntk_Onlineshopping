from django.db import models
from admin_auth.models import *
from user_auth.models import*

# Create your models here.


class Cart(models.Model):
    
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    products=models.ForeignKey(ProductVariant,on_delete=models.SET_NULL,null=True)
    quantity=models.PositiveBigIntegerField(default=0)
    created_date=models.DateField(default=timezone.now)


class Checkout(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0, null=True)
    coupon = models.ForeignKey(Coupons ,on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(UserAdress, on_delete=models.CASCADE, null=True, blank=True)
    payable_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    payment = models.CharField(max_length=100, null=True, blank=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)


    class Meta:
        ordering = ['user']
        

    def __str__(self):
        return f"self.user.email"

    

