from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking, Category
from datetime import date, time


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'description']


class MenuSerializer(serializers.ModelSerializer):
    """Serializer for Menu model"""

    class Meta:
        model = Menu
        fields = [
            'id', 'title', 'price', 'inventory', 'description',
            'category', 'featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_price(self, value):
        """Validate that price is positive"""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_inventory(self, value):
        """Validate that inventory is non-negative"""
        if value < 0:
            raise serializers.ValidationError("Inventory cannot be negative.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    customer_name = serializers.ReadOnlyField()
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'first_name', 'last_name', 'customer_name', 'guest_number',
            'comment', 'reservation_date', 'reservation_time', 'status',
            'user', 'user_email', 'phone_number', 'email', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'user']

    def validate_reservation_date(self, value):
        """Validate that reservation date is not in the past"""
        if value < date.today():
            raise serializers.ValidationError("Reservation date cannot be in the past.")
        return value

    def validate_reservation_time(self, value):
        """Validate reservation time is within business hours"""
        opening_time = time(10, 0)  # 10:00 AM
        closing_time = time(22, 0)  # 10:00 PM

        if value < opening_time or value > closing_time:
            raise serializers.ValidationError(
                "Reservation time must be between 10:00 AM and 10:00 PM."
            )
        return value

    def validate(self, data):
        """Custom validation for the entire booking"""
        reservation_date = data.get('reservation_date')
        reservation_time = data.get('reservation_time')

        # Check if there's already a booking for this date and time
        if reservation_date and reservation_time:
            existing_booking = Booking.objects.filter(
                reservation_date=reservation_date,
                reservation_time=reservation_time
            ).exclude(id=self.instance.id if self.instance else None)

            if existing_booking.exists():
                raise serializers.ValidationError(
                    "This time slot is already booked. Please choose a different time."
                )

        return data

    def create(self, validated_data):
        """Override create to set the user from request"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']
