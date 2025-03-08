# LittleLemonAPI/urls.py

from django.urls import path
from .views import (
    MenuItemList, MenuItemDetail, CategoryListCreate,
    CartItemListCreate, CartItemDelete, OrderListCreate, OrderDetail,
    ManagerGroupList, ManagerGroupDetail,
    DeliveryCrewGroupList, DeliveryCrewGroupDetail,
)

urlpatterns = [
    # Menu items endpoints
    path('menu-items/', MenuItemList.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', MenuItemDetail.as_view(), name='menu-item-detail'),
    # Category endpoints
    path('categories/', CategoryListCreate.as_view(), name='categories-list'),
    # Cart endpoints
    path('cart/menu-items/', CartItemListCreate.as_view(), name='cart-items'),
    path('cart/menu-items/clear/', CartItemDelete.as_view(), name='cart-clear'),
    # Order endpoints
    path('orders/', OrderListCreate.as_view(), name='orders-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    # Manager group endpoints
    path('groups/manager/users/', ManagerGroupList.as_view(), name='manager-group-list'),
    path('groups/manager/users/<int:user_id>/', ManagerGroupDetail.as_view(), name='manager-group-detail'),
    # Delivery crew group endpoints
    path('groups/delivery-crew/users/', DeliveryCrewGroupList.as_view(), name='delivery-group-list'),
    path('groups/delivery-crew/users/<int:user_id>/', DeliveryCrewGroupDetail.as_view(), name='delivery-group-detail'),
]
