from django.urls import path
from . import views
from .views import reservation_form

urlpatterns = [
    path('', reservation_form, name='reservation_form'),  # Reservation form at /restaurant/
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view(), name='booking-list'),
    path('booking/<int:pk>', views.SingleBookingView.as_view(), name='booking-detail'),
]
