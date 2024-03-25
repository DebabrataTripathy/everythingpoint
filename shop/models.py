from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    dis_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Order(models.Model):
    items=models.CharField(max_length=2000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=10)
    total=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    