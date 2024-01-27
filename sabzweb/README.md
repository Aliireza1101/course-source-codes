# Django Blog

Welcome to the **Django Blog** project, an introductory application developed through Sabzlearn's Django course.

## Setting Up the Project

### Prerequisites
Ensure you have Django installed and ready to use. If not, follow the Django official documentation to set it up.

### Timezone Configuration
To configure the application with Iran's local date and time settings, please refer to the following video tutorials:
- [Video Guide 1](https://sabzlearn.ir/lesson/38-25918)
- [Video Guide 2](https://sabzlearn.ir/lesson/38-25919)

### Running the Project
To get the project up and running, follow these steps:

1. Initialize the database:

    ```
    python manage.py migrate
    ```

2. Start the development server:

    ```
    python manage.py runserver
    ```

### Initial Setup
At first, you may experience an error due to an empty database. To resolve this:

1. Create an admin superuser:

    ```
    python manage.py createsuperuser
    ```

2. After creating the superuser, start the server:

    ```
    python manage.py runserver
    ```

3. Log in to the admin panel at: [Admin Panel](http://127.0.0.1:8000/admin/). Use the credentials set during the `createsuperuser` step.

4. Navigate to the post creation URL: [Create Post](http://127.0.0.1:8000/blog/create/).

### Creating Posts
Create a few posts via the [Create Post](http://127.0.0.1:8000/blog/create/) to populate your blog. This step should eliminate any initial errors related to the empty database.

Enjoy developing with Django
