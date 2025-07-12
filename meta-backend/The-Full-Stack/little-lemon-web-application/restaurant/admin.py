from django.contrib import admin
from .models import Menu, Booking, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model"""
    list_display = ['title', 'slug', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Admin configuration for Menu model"""
    list_display = ['title', 'price', 'category', 'inventory', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'description', 'category']
    list_editable = ['price', 'inventory', 'featured']
    ordering = ['title']

    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'inventory')
        }),
        ('Features', {
            'fields': ('featured',)
        }),
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin configuration for Booking model"""
    list_display = [
        'customer_name', 'reservation_date', 'reservation_time',
        'guest_number', 'status', 'phone_number', 'created_at'
    ]
    list_filter = ['status', 'reservation_date', 'guest_number', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    list_editable = ['status']
    ordering = ['-reservation_date', 'reservation_time']

    fieldsets = (
        ('Customer Information', {
            'fields': ('first_name', 'last_name', 'phone_number', 'email', 'user')
        }),
        ('Reservation Details', {
            'fields': ('reservation_date', 'reservation_time', 'guest_number', 'status')
        }),
        ('Additional Information', {
            'fields': ('comment',),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']

    def get_readonly_fields(self, request, obj=None):
        """Make customer name read-only if editing existing booking"""
        readonly_fields = list(self.readonly_fields)
        if obj:  # editing an existing object
            readonly_fields.extend(['reservation_date', 'reservation_time'])
        return readonly_fields


# Customize admin site header and title
admin.site.site_header = "Little Lemon Restaurant Admin"
admin.site.site_title = "Little Lemon Admin Portal"
admin.site.index_title = "Welcome to Little Lemon Restaurant Administration"
