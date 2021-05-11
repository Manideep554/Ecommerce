from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20,null=True)
    description=models.CharField(max_length=50,null=True)

class Product(models.Model):
    name=models.CharField(max_length=20,null=True)
    serialnumber=models.CharField(max_length=20,unique=True)
    price=models.FloatField()
    description=models.CharField(max_length=50,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    image=models.ImageField(upload_to='product_image/')

class UserDetails(models.Model):
    mobile=models.CharField(max_length=13,null=True)
    address=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
