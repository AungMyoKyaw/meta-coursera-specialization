from django.contrib import admin
from .models import Booking, Menu

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'reservation_date', 'reservation_slot', 'created_by')
	list_filter = ('reservation_date', 'reservation_slot', 'created_by')
	search_fields = ('full_name', 'created_by__username')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	search_fields = ('name',)
