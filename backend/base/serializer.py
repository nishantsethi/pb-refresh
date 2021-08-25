from re import L
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


