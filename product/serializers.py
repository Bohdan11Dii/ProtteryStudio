from rest_framework import serializers
from product.models import Category, Color, Product


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        
class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = "__all__"


#Product Serializers

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "quantity", "category", "color" )


class PrdouctListSerializer(ProductSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name"
    )
    color = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class ProductDetailSerializer(ProductSerializer):
    category = CategorySerializer(many=False, read_only=True)
    color = ColorSerializer(many=True, read_only=True)

