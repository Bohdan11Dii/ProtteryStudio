from product.models import Category, Color, Product
from product.serializers import (
    CategorySerializer,
    ColorSerializer,
    ProductSerializer,
    PrdouctListSerializer,
    ProductDetailSerializer,
)
from rest_framework import  viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return PrdouctListSerializer
        if self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer