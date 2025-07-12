from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Define URL patterns for the restaurant app
urlpatterns = [
    # Menu endpoints
    path('menu/', views.MenuListCreateView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu-detail'),

    # Booking endpoints
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),

    # Category endpoints
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    # User endpoints
    path('user/profile/', views.UserProfileView.as_view(), name='user-profile'),

    # Custom authentication endpoints
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),

    # Dashboard/Stats endpoint
    path('dashboard/stats/', views.dashboard_stats, name='dashboard-stats'),
]
