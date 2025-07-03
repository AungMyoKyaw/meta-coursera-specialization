from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrOwner(BasePermission):
    """
    Custom permission to allow admin users full access or object owners to edit/delete.
    """
    def has_permission(self, request, view):
        # Allow any user to list or create bookings
        if view.__class__.__name__ == 'BookingView':
            return True
        # For other views, require authentication
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin users have full access
        if request.user and request.user.is_staff:
            return True
        # Owners can view or edit their own bookings
        return hasattr(obj, 'created_by') and obj.created_by == request.user
