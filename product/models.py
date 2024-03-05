from django.db import models
from typing import Union
# Create your models here.
from django.db.models import Model
from product.utils import product_directory_path


class Category(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Collection(models.Model):
    pass


class Image(models.Model):
    product_id = models.ForeignKey(
        "product.Product",
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ImageField(upload_to = product_directory_path)
    
    def __str__(self) -> str:
        return f"{self.product_id.name} - id {self.product_id.id}"


class Product(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    color = models.ManyToManyField(
        Color,
        related_name="products"
    )
    
    class Meta:
        ordering = ["name"]
        
    def __str__(self) -> str:
        return f"Name {self.name}, (price: {self.price}, quantity: {self.quantity})"



