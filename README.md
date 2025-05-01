# PlantTracker2

This is a **Django REST Framework (DRF)** learning project. The goal of this project is to explore and practice building APIs using Django and DRF. The project includes models, serializers, views, and custom management commands to manage plant-related data.

## Features
- Models for managing plants, species, and transfers.
- RESTful API endpoints for CRUD operations.
- Custom management commands for loading data from CSV files.
- Integration with Django Extensions for enhanced development tools.

---

## Common Commands

### 1. **Run the Development Server**

first time runner, set up the virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

Start the Django development server to test the application locally:
```bash
python manage.py runserver
```

### 2. **Make Migrations**
Create migration files after modifying models:
```bash
python manage.py makemigrations
```

### 3. **Apply Migrations**
Apply the migrations to update the database schema:
```bash
python manage.py migrate
```

### 4. **Run the Shell**
Open the Django shell to interact with models and data:
```bash
python manage.py shell
```

### 5. **Run the Enhanced Shell **
If `django-extensions` is installed, use `shell_plus` for auto-imports:
```bash
python manage.py shell_plus
```

### 6. **Run Tests**
Run the test suite to ensure everything is working as expected:
```bash
python manage.py test
```

### 7. **Load Data from CSV**
Use the custom management command to load species data from a CSV file:
```bash
python manage.py load_species /path/to/species.csv
```

---

## Prerequisites
- Python 3.12+
- Django 5.x
- Django REST Framework
- Django Extensions (optional)

---

## Learning Goals
- Understand how to define models and serializers in Django.
- Learn how to create and manage API endpoints using DRF.
- Practice writing custom management commands.
- Explore database migrations and schema management.
