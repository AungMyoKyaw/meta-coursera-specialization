from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrOwner

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Timeline view: if date provided, show all bookings for that date
        user = self.request.user
        queryset = Booking.objects.all()
        date = self.request.query_params.get('reservation_date')
        if date:
            return queryset.filter(reservation_date=date)
        # No date: list own bookings for authenticated users
        if user and user.is_authenticated and not user.is_staff:
            return queryset.filter(created_by=user)
        # Admin sees all bookings
        if user and user.is_staff:
            return queryset
        # Unauthenticated users: no bookings
        return Booking.objects.none()

class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Retrieve, update, or delete a booking. Permissions restricted to admin or owner.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminOrOwner]

def reservation_form(request):
    # Render booking interface; admin management via Django admin
    return render(request, 'reservations.html')
