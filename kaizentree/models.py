from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=250)
    
class Item(models.Model):
    sku = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=50)
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()
