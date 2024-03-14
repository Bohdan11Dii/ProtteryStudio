from django.contrib import admin
from product.models import Category, Color, Image, Product
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

admin.site.register(Category)
admin.site.register(Color)

