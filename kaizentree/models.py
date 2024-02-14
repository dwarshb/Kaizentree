from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=250)
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    
class Item(models.Model):
    sku = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
