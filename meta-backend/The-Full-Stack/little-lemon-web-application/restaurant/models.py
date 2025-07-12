from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Menu(models.Model):
    """Menu model to store menu items"""
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    inventory = models.SmallIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, default='Main Course')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f"{self.title} - ${self.price}"


class Booking(models.Model):
    """Booking model to store table reservations"""
    PARTY_SIZE_CHOICES = [
        (1, '1 person'),
        (2, '2 people'),
        (3, '3 people'),
        (4, '4 people'),
        (5, '5 people'),
        (6, '6 people'),
        (7, '7 people'),
        (8, '8 people'),
        (9, '9 people'),
        (10, '10 people'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    guest_number = models.SmallIntegerField(choices=PARTY_SIZE_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.CharField(max_length=1000, blank=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['reservation_date', 'reservation_time']
        unique_together = ['reservation_date', 'reservation_time']
        verbose_name = 'Table Booking'
        verbose_name_plural = 'Table Bookings'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date} at {self.reservation_time}"

    @property
    def customer_name(self):
        """Return full customer name"""
        return f"{self.first_name} {self.last_name}".strip()


class Category(models.Model):
    """Category model for menu items"""
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
