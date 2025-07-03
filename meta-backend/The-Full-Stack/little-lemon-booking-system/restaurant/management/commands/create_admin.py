import getpass
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create an admin user'

    def handle(self, *args, **options):
        User = get_user_model()
        self.stdout.write('Creating admin user...')
        username = input('Username: ').strip()
        if not username:
            raise CommandError('Username cannot be blank')

        email = input('Email: ').strip()
        if not email or '@' not in email:
            raise CommandError('Enter a valid email')

        if User.objects.filter(username=username).exists():
            raise CommandError(f"Username '{username}' already exists")

        password = getpass.getpass('Password: ')
        password2 = getpass.getpass('Password (again): ')
        if password != password2:
            raise CommandError('Passwords do not match')
        if len(password) < 8:
            raise CommandError('Password must be at least 8 characters long')

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Admin user '{username}' created successfully"))
