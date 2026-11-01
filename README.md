# CarsRental — LAB_APPS_VIEWS

A simple Django project created to practice apps, views, and URL routing. The project contains one custom app named `rentals`.

## Pages

| Path                  | Description                               |
| --------------------- | ----------------------------------------- |
| `/`                   | Displays the home welcome message.        |
| `/about/`             | Displays a short text about car rentals.  |
| `/password/generate/` | Generates a random 10-character password. |

### Home Page

Returns the following message:

```text
Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.
```

### About Page

Returns the following text:

```text
A simple paragraph about Car Rentals.
```

### Password Generator — Bonus

Generates a random password containing uppercase letters, lowercase letters, numbers, and symbols.

Refresh the page to generate a new password.

## Run the Project

From the repository folder, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the dependencies and start the development server:

```powershell
python -m pip install -r requirements.txt
cd CarsRental
python manage.py runserver
```

Open these URLs in your browser:

- Home: http://127.0.0.1:8000/
- About: http://127.0.0.1:8000/about/
- Password Generator: http://127.0.0.1:8000/password/generate/

To stop the server, press `Ctrl + C`.

## Project Structure

```text
CarsRental/
├── manage.py
├── CarsRental/
│   ├── settings.py
│   └── urls.py
└── rentals/
    ├── __init__.py
    ├── apps.py
    ├── urls.py
    └── views.py
```

## Validation

- Django system checks passed.
- All three pages returned successful responses.
- Password generation was checked for length and required character types.
