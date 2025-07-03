# Little Lemon Booking System

Welcome to the **Little Lemon Booking System**! This web application allows restaurant visitors to make table reservations online, and lets administrators manage bookings and menu items.

---

## Features

-   **User-Friendly Reservations**: A public-facing page for anyone to reserve a table for a specific date and time.
-   **Admin Dashboard**: A secure admin panel for staff to manage all bookings and menu items.
-   **RESTful API**: A comprehensive API for programmatic access to create, view, and manage bookings and menu entries.
-   **Dynamic Timeline**: Shows a live timeline of bookings for any selected date.

---

## Project Structure

```
.
├── manage.py               # Django command-line utility
├── db.sqlite3              # Local SQLite database (auto-generated)
├── little_lemon/           # Django project settings and URL config
│   ├── settings.py         # Configuration (INSTALLED_APPS, DB, static files)
│   ├── urls.py             # Root URL routes
│   └── ...
├── restaurant/             # Django app for bookings and menu
│   ├── models.py           # Database models: Booking, Menu
│   ├── views.py            # API endpoints and reservation page view
│   ├── serializers.py      # Converts models to/from JSON
│   ├── permissions.py      # Custom access rules for bookings
│   ├── urls.py             # App-specific URL routes
│   ├── templates/          # HTML template for reservation page
│   └── migrations/         # Database schema history
└── .gitignore              # Files and folders ignored by Git
```

---

## Prerequisites

-   Python 3.8+
-   `pip` (Python package manager)
-   `venv` (Recommended for virtual environments)

---

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd little-lemon-booking-system
```

### 2. Create and Activate a Virtual Environment

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install Django djangorestframework djoser djangorestframework-simplejwt
```
*(Note: If a `requirements.txt` file is provided, you can run `pip install -r requirements.txt` instead.)*

### 4. Apply Database Migrations

This command sets up the database tables and seeds the initial menu items.

```bash
python manage.py migrate
```

### 5. Create an Admin Superuser

You'll need an admin account to access the Django admin dashboard.

```bash
python manage.py createsuperuser
```
Follow the prompts to set up your username, email, and a secure password.

### 6. Run the Development Server

```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

---

## How to Use

### Public Reservation Page

1.  Navigate to `http://127.0.0.1:8000/`.
2.  Choose a date and an available time slot.
3.  Click **Book** to submit your reservation.

### Admin Dashboard

1.  Navigate to `http://127.0.0.1:8000/admin/`.
2.  Log in with your superuser credentials.
3.  Manage **Bookings** and **Menu** items directly from the dashboard.

### API Endpoints

The API is available under the `/restaurant/` path.

-   **Menu Items**:
    -   `GET /restaurant/menu/` - List all menu items.
    -   `POST /restaurant/menu/` - Create a new menu item.
    -   `GET /restaurant/menu/{id}/` - Retrieve a single menu item.
-   **Bookings**:
    -   `GET /restaurant/booking/` - List all bookings.
    -   `POST /restaurant/booking/` - Create a new booking.
    -   `GET /restaurant/booking/{id}/` - Retrieve a single booking.

#### API Authentication

The API uses JWT for authentication.

1.  **Obtain a token**:
    ```bash
    POST /auth/jwt/create/
    Payload: { "username": "<your-username>", "password": "<your-password>" }
    ```
2.  **Use the token**: Include the token in the `Authorization` header for all API requests.
    ```
    Authorization: Bearer <your-token>
    ```

---

## Running Tests

To run the automated tests for the API and models, use the following command:

```bash
python manage.py test
```

---

## Resetting the Database

To clear all data and start fresh:
1.  Stop the server.
2.  Delete the `db.sqlite3` file.
3.  Run the migrations again:
    ```bash
    python manage.py migrate
    ```

> **Questions or Issues?**
> Feel free to open an issue or reach out to the maintainers. Thank you for trying the Little Lemon Booking System!