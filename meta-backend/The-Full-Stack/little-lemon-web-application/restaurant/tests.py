from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from datetime import date, time
from decimal import Decimal
from .models import Menu, Booking, Category
from .serializers import MenuSerializer, BookingSerializer


class MenuModelTest(TestCase):
    """Test cases for Menu model"""

    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Grilled Chicken",
            price=Decimal('15.99'),
            inventory=10,
            description="Delicious grilled chicken with herbs",
            category="Main Course"
        )

    def test_menu_creation(self):
        """Test menu item creation"""
        self.assertEqual(self.menu_item.title, "Grilled Chicken")
        self.assertEqual(self.menu_item.price, Decimal('15.99'))
        self.assertEqual(self.menu_item.inventory, 10)
        self.assertEqual(str(self.menu_item), "Grilled Chicken - $15.99")

    def test_menu_str_representation(self):
        """Test string representation of menu item"""
        expected = "Grilled Chicken - $15.99"
        self.assertEqual(str(self.menu_item), expected)


class BookingModelTest(TestCase):
    """Test cases for Booking model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.booking = Booking.objects.create(
            first_name="John",
            last_name="Doe",
            guest_number=4,
            reservation_date=date(2024, 12, 25),
            reservation_time=time(19, 30),
            user=self.user,
            phone_number="123-456-7890"
        )

    def test_booking_creation(self):
        """Test booking creation"""
        self.assertEqual(self.booking.first_name, "John")
        self.assertEqual(self.booking.last_name, "Doe")
        self.assertEqual(self.booking.guest_number, 4)
        self.assertEqual(self.booking.user, self.user)

    def test_customer_name_property(self):
        """Test customer_name property"""
        self.assertEqual(self.booking.customer_name, "John Doe")

    def test_booking_str_representation(self):
        """Test string representation of booking"""
        expected = "John Doe - 2024-12-25 at 19:30:00"
        self.assertEqual(str(self.booking), expected)


class MenuAPITest(APITestCase):
    """Test cases for Menu API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)

        self.menu_item = Menu.objects.create(
            title="Test Pizza",
            price=Decimal('12.99'),
            inventory=5,
            description="Test pizza description",
            category="Pizza"
        )

    def test_get_menu_list_unauthenticated(self):
        """Test getting menu list without authentication"""
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_menu_item_detail(self):
        """Test getting menu item detail"""
        url = reverse('menu-detail', kwargs={'pk': self.menu_item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Pizza")

    def test_create_menu_item_authenticated(self):
        """Test creating menu item with authentication"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('menu-list')
        data = {
            'title': 'New Burger',
            'price': '10.99',
            'inventory': 8,
            'description': 'Tasty burger',
            'category': 'Burgers'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)

    def test_create_menu_item_unauthenticated(self):
        """Test creating menu item without authentication"""
        url = reverse('menu-list')
        data = {
            'title': 'New Burger',
            'price': '10.99',
            'inventory': 8,
            'description': 'Tasty burger',
            'category': 'Burgers'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_menu_item_authenticated(self):
        """Test updating menu item with authentication"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('menu-detail', kwargs={'pk': self.menu_item.pk})
        data = {
            'title': 'Updated Pizza',
            'price': '15.99',
            'inventory': 3,
            'description': 'Updated description',
            'category': 'Pizza'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item.refresh_from_db()
        self.assertEqual(self.menu_item.title, 'Updated Pizza')

    def test_delete_menu_item_authenticated(self):
        """Test deleting menu item with authentication"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('menu-detail', kwargs={'pk': self.menu_item.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)


class BookingAPITest(APITestCase):
    """Test cases for Booking API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.booking = Booking.objects.create(
            first_name="Jane",
            last_name="Smith",
            guest_number=2,
            reservation_date=date(2024, 12, 31),
            reservation_time=time(20, 0),
            user=self.user,
            phone_number="098-765-4321"
        )

    def test_get_booking_list_authenticated(self):
        """Test getting booking list with authentication"""
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_booking_list_unauthenticated(self):
        """Test getting booking list without authentication"""
        self.client.credentials()  # Remove credentials
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_booking_authenticated(self):
        """Test creating booking with authentication"""
        url = reverse('booking-list')
        data = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'guest_number': 3,
            'reservation_date': '2024-12-20',
            'reservation_time': '18:30:00',
            'phone_number': '555-123-4567'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_get_booking_detail(self):
        """Test getting booking detail"""
        url = reverse('booking-detail', kwargs={'pk': self.booking.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')

    def test_update_booking(self):
        """Test updating booking"""
        url = reverse('booking-detail', kwargs={'pk': self.booking.pk})
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith-Updated',
            'guest_number': 4,
            'reservation_date': '2024-12-31',
            'reservation_time': '20:00:00',
            'phone_number': '098-765-4321',
            'status': 'confirmed'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.last_name, 'Smith-Updated')
        self.assertEqual(self.booking.guest_number, 4)

    def test_delete_booking(self):
        """Test deleting booking"""
        url = reverse('booking-detail', kwargs={'pk': self.booking.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)


class AuthenticationAPITest(APITestCase):
    """Test cases for Authentication API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            're_password': 'newpass123'
        }

    def test_user_registration(self):
        """Test user registration"""
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Test user login"""
        # First create a user
        User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Then try to login
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post('/api/auth/token/login/', login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)


class SerializerTest(TestCase):
    """Test cases for serializers"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_menu_serializer_valid_data(self):
        """Test MenuSerializer with valid data"""
        data = {
            'title': 'Test Dish',
            'price': '19.99',
            'inventory': 5,
            'description': 'Test description',
            'category': 'Test Category'
        }
        serializer = MenuSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_menu_serializer_invalid_price(self):
        """Test MenuSerializer with invalid price"""
        data = {
            'title': 'Test Dish',
            'price': '-5.00',  # Invalid negative price
            'inventory': 5,
            'description': 'Test description',
            'category': 'Test Category'
        }
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_booking_serializer_valid_data(self):
        """Test BookingSerializer with valid data"""
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'guest_number': 4,
            'reservation_date': '2024-12-25',
            'reservation_time': '19:30:00',
            'phone_number': '123-456-7890'
        }
        serializer = BookingSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_booking_serializer_past_date(self):
        """Test BookingSerializer with past reservation date"""
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'guest_number': 4,
            'reservation_date': '2020-01-01',  # Past date
            'reservation_time': '19:30:00',
            'phone_number': '123-456-7890'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('reservation_date', serializer.errors)

    def test_booking_serializer_invalid_time(self):
        """Test BookingSerializer with invalid reservation time"""
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'guest_number': 4,
            'reservation_date': '2024-12-25',
            'reservation_time': '05:00:00',  # Too early (before 10 AM)
            'phone_number': '123-456-7890'
        }
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('reservation_time', serializer.errors)
