from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'reservation_date', 'reservation_slot']
        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=['reservation_date', 'reservation_slot'],
                message="This time slot is already booked for the selected date."
            )
        ]
