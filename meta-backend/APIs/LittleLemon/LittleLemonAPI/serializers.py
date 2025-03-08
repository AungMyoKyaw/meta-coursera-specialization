# LittleLemonAPI/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, MenuItem, CartItem, Order, OrderItem

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']

class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), source='menu_item', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity']

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    delivery_crew = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'created_at', 'order_items']
