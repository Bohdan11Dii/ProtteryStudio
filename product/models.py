from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
