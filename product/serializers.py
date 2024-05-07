from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'detail', 'price', 'user_id')
        extra_kwargs = {'user_id': {'write_only': True}}