from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
]