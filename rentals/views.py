from django.shortcuts import render

# Create your views here.
import secrets
import string

from django.http import HttpResponse
from django.views.decorators.cache import never_cache


def home(request):
    return HttpResponse(
        "Hello World, This is my new HOME for Car Rentals Website  ! "
        "we're excited to welcome you here.",
        content_type="text/plain",
    )


def about(request):
    return HttpResponse(
        "A simple paragraph about Car Rentals. ",
        content_type="text/plain",
    )


@never_cache
def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = "".join(
            secrets.choice(characters) for _ in range(10)
        )

        if (
            any(char in string.ascii_lowercase for char in password)
            and any(char in string.ascii_uppercase for char in password)
            and any(char in string.digits for char in password)
            and any(char in string.punctuation for char in password)
        ):
            return HttpResponse(password, content_type="text/plain")