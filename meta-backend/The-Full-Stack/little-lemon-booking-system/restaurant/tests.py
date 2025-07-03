from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Booking
import datetime


User = get_user_model()

class BookingAPITests(APITestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='pass1234')
        self.user2 = User.objects.create_user(username='user2', password='pass1234')
        self.admin = User.objects.create_superuser(username='admin', email='admin@test.com', password='adminpass')
        self.client = APIClient()
        # Create a booking by user1
        self.booking = Booking.objects.create(
            full_name='Test',
            reservation_date=datetime.date.today(),
            reservation_slot='12:00 PM',
            created_by=self.user1
        )

    def test_user_can_view_own_booking(self):
        self.client.login(username='user1', password='pass1234')
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_user_cannot_view_others_booking(self):
        self.client.login(username='user2', password='pass1234')
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_admin_can_view_all_bookings(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_user_cannot_delete_others_booking(self):
        self.client.login(username='user2', password='pass1234')
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)

    def test_user_can_delete_own_booking(self):
        self.client.login(username='user1', password='pass1234')
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_admin_can_delete_any_booking(self):
        self.client.login(username='admin', password='adminpass')
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
