# Little Lemon Django Web App

This project is a Django web application for the Little Lemon restaurant, featuring menu management, booking, and more.

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- venv (Recommended for virtual environments)

## Setup Instructions

1. **Clone the repository and navigate to the project directory:**

   ```bash
   git clone <repository-url>
   cd littlelemon
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   # Or use requirements.txt if available:
   # pip install -r requirements.txt
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The app will be available at http://127.0.0.1:8000/

## Project Structure

- `manage.py`: Django management script
- `littlelemon/`: Project settings and configuration
- `menu/`: Menu app
- `media/`, `templates/`: Static and template files

## License

MIT
