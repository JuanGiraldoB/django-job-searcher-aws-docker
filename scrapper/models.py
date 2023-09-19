from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
