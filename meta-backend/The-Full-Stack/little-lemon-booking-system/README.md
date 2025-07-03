# Little Lemon Booking System

This is a Django project for the Little Lemon Booking System.

## How to Run the Project

Follow these steps to set up and run the project locally:

1.  **Install Dependencies**

    It is recommended to use a virtual environment. First, create and activate one:

    ```bash
     # Little Lemon Booking System

     Welcome to the **Little Lemon Booking System**! This web application allows restaurant visitors to make table reservations online, and lets administrators manage bookings and menu items.

     ---

     ## What You Will Learn

     - How to set up and run a Django project
     - How to use a REST API for creating, viewing, and deleting bookings and menu entries
     - How a simple front-end reservation page works

     ---

     ## Project Overview

     The project consists of two main parts:

     1. **Public Reservation Page**
         - A user-friendly web page where anyone can select a date and time slot, then submit a reservation.
         - Shows a live timeline of bookings for the selected date.

     2. **Django REST API & Admin Interface**
         - API endpoints to list, create, update, and delete `Booking` and `Menu` data.
         - Admin dashboard (built-in Django admin) for full control over all data.

     ---

     ## Code Structure

    ```

    ├── manage.py # Django command-line utility
    ├── db.sqlite3 # Local SQLite database (auto-generated)
    ├── little_lemon/ # Django project settings and URL config
    │ ├── settings.py # Configuration (INSTALLED_APPS, DB, static files)
    │ ├── urls.py # Root URL routes
    │ ├── wsgi.py, asgi.py # Server entry points
    │
    ├── restaurant/ # Django app for bookings and menu
    │ ├── models.py # Database models: Booking, Menu
    │ ├── views.py # API endpoints and reservation page view
    │ ├── serializers.py # Convert models to/from JSON
    │ ├── permissions.py # Custom rules: who can view/edit bookings
    │ ├── urls.py # App-specific URL routes
    │ ├── templates/ # HTML template for reservation page
    │ ├── static/ # CSS styles for the page
    │ └── migrations/ # Database schema changes history
    │
    └── .gitignore # Files and folders ignored by Git

    ````

    - **Booking model**: stores reservations (name, date, slot, creator).
    - **Menu model**: stores restaurant menu items (name, price, description). Initial items are seeded via migrations.

    ---

    ## Prerequisites

    - macOS, Windows, or Linux with a terminal/shell
    - **Python 3.8+** installed. Check with:
       ```bash
       python3 --version
       ```
    - **pip** (Python package manager)
    - (Recommended) **virtual environment** tool (`venv`)

    ---

    ## Step-by-Step Setup

    ### 1. Clone the Repository
    ```bash
    git clone <repository-url>
    cd little-lemon-booking-system
    ````

    ### 2. Create and Activate a Virtual Environment

    ```bash
    python3 -m venv venv         # Create virtual environment folder
    source venv/bin/activate     # Activate it (use `venv\Scripts\activate` on Windows)
    ```

    ### 3. Install Dependencies

    If a `requirements.txt` file exists:

    ```bash
    pip install -r requirements.txt
    ```

    Otherwise install manually:

    ```bash
    pip install Django djangorestframework djoser djangorestframework-simplejwt
    ```

    ### 4. Apply Database Migrations

    This sets up tables and seeds initial menu items:

    ```bash
    python manage.py migrate
    ```

    ### 5. Create an Admin (Superuser)

    To access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts for username, email, and password (minimum 8 characters).

    ### 6. Run the Development Server

    Start the app locally:

    ```bash
    python manage.py runserver
    ```

    Open your browser to `http://127.0.0.1:8000/` to see the reservation page.

    ***

    ## How to Use

    ### Public Reservation Interface
    1.  Choose a **date** (defaults to today).
    2.  Select an available **time slot**.
    3.  Click **Book**.
    4.  See confirmation message, total bookings count, and a timeline of reservations.

    ### Admin Dashboard
    1.  Go to `http://127.0.0.1:8000/admin/`.
    2.  Log in with your superuser credentials.
    3.  Manage **Bookings** and **Menu** items (view, add, edit, delete).

    ### API Endpoints
    - **Menu Items**:
      - List/Create: `GET/POST /restaurant/menu/`
      - Retrieve/Update/Delete: `GET/PUT/PATCH/DELETE /restaurant/menu/<id>/`
    - **Bookings**:
      - List/Create: `GET/POST /restaurant/booking/`
        - Add `?reservation_date=YYYY-MM-DD` to list all bookings for a given date.
      - Retrieve/Update/Delete: `GET/PUT/PATCH/DELETE /restaurant/booking/<id>/`

    #### Authentication

    The API uses JWT tokens:
    1.  Obtain token:
        ```bash
        POST /auth/jwt/create/
        Payload: { "username": "<your-username>", "password": "<your-password>" }
        ```
    2.  Include in headers:
        ```
        Authorization: Bearer <your-token>
        ```

    ***

    ## Running Tests

    To run automated tests (API and model tests):

    ```bash
    python manage.py test
    ```

    ***

    ## Resetting the Database

    To start fresh:
    1.  Stop the server.
    2.  Delete `db.sqlite3` file.
    3.  Run:
        ```bash
        python manage.py migrate
        ```

    ***

    > **Questions or Issues?**  
    > Feel free to open an issue or reach out to the maintainers. Thank you for trying Little Lemon Booking System!
