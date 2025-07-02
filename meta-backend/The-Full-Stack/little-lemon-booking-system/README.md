# Little Lemon Booking System

This is a Django project for the Little Lemon Booking System.

## How to Run the Project

Follow these steps to set up and run the project locally:

1.  **Install Dependencies**

    It is recommended to use a virtual environment. First, create and activate one:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

    Then, install the required Python packages. If a `requirements.txt` file is not provided, you can install the common dependencies:

    ```bash
    pip install Django djangorestframework djoser
    ```

2.  **Run Database Migrations**

    Apply the database migrations to set up the necessary tables:

    ```bash
    python manage.py migrate
    ```

3.  **Create a Superuser (Optional)**

    To access the Django admin panel, you can create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up a username, email, and password.

4.  **Run the Development Server**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

    The application will typically be available at `http://127.0.0.1:8000/`.
