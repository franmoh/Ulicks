from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True, serialize=True, unique=True)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=100, primary_key=True, serialize=True, unique=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id