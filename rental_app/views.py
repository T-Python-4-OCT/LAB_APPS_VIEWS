import secrets
import string

from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    )


def about(request):
    return HttpResponse("A simple paragraph about Car Rentals. ")


def password_generator(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(10))
    return HttpResponse(password)
