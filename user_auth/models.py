from django.db import models
from admin_auth.models import *

# Create your models here.




class UserAdress(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=150,blank=True)
    last_name=models.CharField(max_length=150,blank=True)
    phonenumber=models.CharField(blank=True)
    address=models.CharField(max_length=150,null=True)
    town=models.CharField(max_length=150,null=False)
    zip_code=models.IntegerField(null=False)
    nearbylocation=models.CharField(max_length=100,blank=True)
    district = models.CharField(max_length=150, null=False)
    created=models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.user.email}"

class Wishlist(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(ProductVariant,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    check_color=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):

        return f"Wishlist item for {self.product}"



class Payementwallet(models.Model):

    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    paymenttype=models.CharField(max_length=150,blank=True,null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"PaymentWallet for User: {self.user}, Payment Type: {self.paymenttype}, Created on: {self.created}"







