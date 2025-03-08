from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name}"

class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        (0, 'Out for delivery'),
        (1, 'Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name} in Order #{self.order.id}"
