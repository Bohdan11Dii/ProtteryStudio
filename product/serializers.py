from rest_framework import serializers
from product.models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256, required=True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance