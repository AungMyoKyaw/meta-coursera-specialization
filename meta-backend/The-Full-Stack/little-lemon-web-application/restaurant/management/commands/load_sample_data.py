from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking, Category
from decimal import Decimal
from datetime import date, time


class Command(BaseCommand):
    help = 'Load sample data for Little Lemon Restaurant'

    # Constants
    APPETIZERS = 'Appetizers'
    MAIN_COURSES = 'Main Courses'
    DESSERTS = 'Desserts'
    BEVERAGES = 'Beverages'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading sample data...'))

        self.create_categories()
        self.create_menu_items()
        self.create_users()
        self.create_bookings()

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))
        self.stdout.write(self.style.WARNING('Admin user created: username="admin", password="admin123"'))

    def create_categories(self):
        """Create sample categories"""
        categories = [
            {'title': self.APPETIZERS, 'slug': 'appetizers', 'description': 'Start your meal with these delicious appetizers'},
            {'title': self.MAIN_COURSES, 'slug': 'main-courses', 'description': 'Hearty and satisfying main dishes'},
            {'title': self.DESSERTS, 'slug': 'desserts', 'description': 'Sweet treats to end your meal'},
            {'title': self.BEVERAGES, 'slug': 'beverages', 'description': 'Refreshing drinks and beverages'},
        ]

        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                title=cat_data['title'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.title}')

    def create_menu_items(self):
        """Create sample menu items"""
        menu_items = [
            {
                'title': 'Greek Salad',
                'price': Decimal('12.99'),
                'inventory': 20,
                'description': 'Fresh vegetables with feta cheese, olives, and Greek dressing',
                'category': self.APPETIZERS,
                'featured': True
            },
            {
                'title': 'Bruschetta',
                'price': Decimal('8.99'),
                'inventory': 15,
                'description': 'Toasted bread topped with fresh tomatoes, basil, and garlic',
                'category': self.APPETIZERS,
                'featured': False
            },
            {
                'title': 'Grilled Branzino',
                'price': Decimal('24.99'),
                'inventory': 10,
                'description': 'Fresh Mediterranean sea bass grilled to perfection with lemon and herbs',
                'category': self.MAIN_COURSES,
                'featured': True
            },
            {
                'title': 'Lemon Dessert',
                'price': Decimal('6.99'),
                'inventory': 25,
                'description': 'Traditional Italian lemon dessert with fresh cream',
                'category': self.DESSERTS,
                'featured': True
            },
            {
                'title': 'Pasta',
                'price': Decimal('18.99'),
                'inventory': 30,
                'description': 'Homemade pasta with your choice of sauce',
                'category': self.MAIN_COURSES,
                'featured': False
            },
            {
                'title': 'Tiramisu',
                'price': Decimal('8.99'),
                'inventory': 12,
                'description': 'Classic Italian dessert with coffee-soaked ladyfingers and mascarpone',
                'category': self.DESSERTS,
                'featured': False
            },
            {
                'title': 'Mediterranean Wine',
                'price': Decimal('35.99'),
                'inventory': 8,
                'description': 'Fine red wine from the Mediterranean region',
                'category': self.BEVERAGES,
                'featured': False
            },
            {
                'title': 'Fresh Lemonade',
                'price': Decimal('4.99'),
                'inventory': 50,
                'description': 'Freshly squeezed lemonade with mint',
                'category': self.BEVERAGES,
                'featured': False
            },
        ]

        for item_data in menu_items:
            menu_item, created = Menu.objects.get_or_create(
                title=item_data['title'],
                defaults=item_data
            )
            if created:
                self.stdout.write(f'Created menu item: {menu_item.title}')

    def create_users(self):
        """Create sample users"""
        sample_users = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'password': 'samplepass123'
            },
            {
                'username': 'jane_smith',
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'password': 'samplepass123'
            },
            {
                'username': 'admin',
                'email': 'admin@littlelemon.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'password': 'admin123',
                'is_staff': True,
                'is_superuser': True
            }
        ]

        for user_data in sample_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    password=user_data['password']
                )
                if user_data.get('is_staff'):
                    user.is_staff = True
                if user_data.get('is_superuser'):
                    user.is_superuser = True
                user.save()
                self.stdout.write(f'Created user: {user.username}')

    def create_bookings(self):
        """Create sample bookings"""
        john = User.objects.get(username='john_doe')
        jane = User.objects.get(username='jane_smith')

        sample_bookings = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'guest_number': 4,
                'reservation_date': date(2024, 12, 25),
                'reservation_time': time(19, 30),
                'status': 'confirmed',
                'user': john,
                'phone_number': '555-0123',
                'email': 'john@example.com',
                'comment': 'Christmas dinner reservation'
            },
            {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'guest_number': 2,
                'reservation_date': date(2024, 12, 31),
                'reservation_time': time(20, 0),
                'status': 'pending',
                'user': jane,
                'phone_number': '555-0456',
                'email': 'jane@example.com',
                'comment': 'New Year\'s Eve celebration'
            },
            {
                'first_name': 'Michael',
                'last_name': 'Johnson',
                'guest_number': 6,
                'reservation_date': date(2024, 12, 20),
                'reservation_time': time(18, 0),
                'status': 'confirmed',
                'user': None,
                'phone_number': '555-0789',
                'email': 'michael@example.com',
                'comment': 'Family dinner'
            }
        ]

        for booking_data in sample_bookings:
            booking, created = Booking.objects.get_or_create(
                reservation_date=booking_data['reservation_date'],
                reservation_time=booking_data['reservation_time'],
                defaults=booking_data
            )
            if created:
                self.stdout.write(f'Created booking: {booking.customer_name} - {booking.reservation_date}')
