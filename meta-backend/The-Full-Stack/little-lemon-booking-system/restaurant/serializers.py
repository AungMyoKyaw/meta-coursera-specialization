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
        fields = ['id', 'full_name', 'reservation_date', 'reservation_slot']
        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=['reservation_date', 'reservation_slot'],
                message="This time slot is already booked for the selected date."
            )
        ]

    def create(self, validated_data):
        request = self.context.get('request', None)
        user = request.user if request and request.user.is_authenticated else None
        return Booking.objects.create(created_by=user, **validated_data)
