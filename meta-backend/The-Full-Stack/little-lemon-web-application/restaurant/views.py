from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Menu, Booking, Category
from .serializers import MenuSerializer, BookingSerializer, CategorySerializer, UserSerializer


# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    """List all categories or create a new category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# Menu Views
class MenuListCreateView(generics.ListCreateAPIView):
    """List all menu items or create a new menu item"""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]  # Allow anyone to view menu

    def get_queryset(self):
        """Filter menu items by category if specified"""
        queryset = Menu.objects.all()
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)

        if category is not None:
            queryset = queryset.filter(category__icontains=category)
        if featured is not None:
            queryset = queryset.filter(featured=True)

        return queryset

    def get_permissions(self):
        """Set permissions based on action"""
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a menu item"""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        """Set permissions based on action"""
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


# Booking Views
class BookingListCreateView(generics.ListCreateAPIView):
    """List all bookings or create a new booking"""
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return bookings for the current user only"""
        if self.request.user.is_staff:
            # Staff can see all bookings
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a booking"""
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return bookings for the current user only"""
        if self.request.user.is_staff:
            # Staff can see all bookings
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)


# User Views
class UserProfileView(generics.RetrieveUpdateAPIView):
    """Retrieve or update user profile"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# Custom Authentication Views
@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    """Custom login view that returns user data along with token"""
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            })
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(
            {'error': 'Username and password required'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def custom_logout(request):
    """Custom logout view that deletes the user's token"""
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'})
    except Token.DoesNotExist:
        return Response(
            {'error': 'Error logging out'},
            status=status.HTTP_400_BAD_REQUEST
        )


# Dashboard/Stats Views
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Get dashboard statistics (for staff users)"""
    if not request.user.is_staff:
        return Response(
            {'error': 'Permission denied'},
            status=status.HTTP_403_FORBIDDEN
        )

    total_menu_items = Menu.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='pending').count()
    featured_items = Menu.objects.filter(featured=True).count()

    return Response({
        'total_menu_items': total_menu_items,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'featured_items': featured_items,
    })
