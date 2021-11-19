from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    feedback=models.TextField(max_length=5000)
    def __str__(self):
        return self.feedback

class IceCream(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="ice-Creams")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="static/Delicious_Images",default="")
    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    order_id=models.AutoField
    items_json=models.TextField(max_length=50000)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    phone=models.CharField(max_length=13)
    amount=models.IntegerField(default=0)
    pincode=models.CharField(max_length=8,default="")
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.fname +' '+ self.lname +' On Date: '+ str(self.timestamp)