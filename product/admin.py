from django.contrib import admin
from product.models import Category, Color, Image, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Product)
