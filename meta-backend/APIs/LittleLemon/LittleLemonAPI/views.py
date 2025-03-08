# LittleLemonAPI/views.py

from rest_framework import generics, status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404

from .models import MenuItem, CartItem, Order, OrderItem, Category
from .serializers import MenuItemSerializer, CartItemSerializer, OrderSerializer, CategorySerializer

# --- Custom Permissions ---
class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists() or request.user.is_superuser

class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery crew').exists() or request.user.is_superuser

# --- Menu Items Endpoints ---

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    search_fields = ['name', 'description']

    def get_permissions(self):
        # Only managers can POST new items.
        if self.request.method == 'POST':
            return [IsManager()]
        return [permissions.AllowAny()]

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        # Only managers can update or delete.
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsManager()]
        return [permissions.AllowAny()]

# --- Category Endpoints (Admin adds categories via admin panel or add similar endpoints) ---

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            # Only admin users can create categories.
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

# --- Cart Endpoints (for Customers) ---
class CartItemListCreate(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDelete(generics.DestroyAPIView):
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- Order Endpoints ---
class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Customers see only their orders, managers see all.
        if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=self.request.user)
        else:
            return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # When creating an order, transfer all current cart items to order items.
        order = serializer.save(user=self.request.user)
        cart_items = CartItem.objects.filter(user=self.request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, menu_item=item.menu_item, quantity=item.quantity)
        cart_items.delete()

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        order = get_object_or_404(Order, pk=self.kwargs['pk'])
        # Ensure customers can only access their own orders.
        if self.request.user.groups.filter(name='Manager').exists() or self.request.user.is_superuser:
            return order
        elif self.request.user.groups.filter(name='Delivery crew').exists():
            if order.delivery_crew == self.request.user:
                return order
        elif order.user == self.request.user:
            return order
        self.permission_denied(self.request, message="Not allowed to access this order")
        return order

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            # Allow managers to update (e.g., assign delivery crew and update status) and delivery crew to update order status.
            if self.request.user.groups.filter(name='Manager').exists():
                return [IsManager()]
            elif self.request.user.groups.filter(name='Delivery crew').exists():
                return [IsDeliveryCrew()]
        return [permissions.IsAuthenticated()]

# --- User Group Management Endpoints ---
# For Manager Group
class ManagerGroupList(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        manager_group = Group.objects.get(name='Manager')
        managers = manager_group.user_set.all()
        data = [{'id': user.id, 'username': user.username} for user in managers]
        return Response(data)

    def post(self, request):
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        manager_group = Group.objects.get(name='Manager')
        manager_group.user_set.add(user)
        return Response({'message': f"User {user.username} added to Manager group."}, status=status.HTTP_201_CREATED)

class ManagerGroupDetail(APIView):
    permission_classes = [IsManager]

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        manager_group = Group.objects.get(name='Manager')
        if user in manager_group.user_set.all():
            manager_group.user_set.remove(user)
            return Response({'message': f"User {user.username} removed from Manager group."})
        return Response({'error': 'User not in Manager group.'}, status=status.HTTP_404_NOT_FOUND)

# For Delivery Crew Group
class DeliveryCrewGroupList(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        delivery_group = Group.objects.get(name='Delivery crew')
        crew = delivery_group.user_set.all()
        data = [{'id': user.id, 'username': user.username} for user in crew]
        return Response(data)

    def post(self, request):
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        delivery_group = Group.objects.get(name='Delivery crew')
        delivery_group.user_set.add(user)
        return Response({'message': f"User {user.username} added to Delivery Crew."}, status=status.HTTP_201_CREATED)

class DeliveryCrewGroupDetail(APIView):
    permission_classes = [IsManager]

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        delivery_group = Group.objects.get(name='Delivery crew')
        if user in delivery_group.user_set.all():
            delivery_group.user_set.remove(user)
            return Response({'message': f"User {user.username} removed from Delivery Crew."})
        return Response({'error': 'User not in Delivery Crew.'}, status=status.HTTP_404_NOT_FOUND)
