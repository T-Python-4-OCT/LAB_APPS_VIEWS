import secrets
import string
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)


def about_view(request: HttpRequest) -> HttpResponse:
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

# Bonus: make a different random 10-character password per request.
def password_generate_view(request: HttpRequest) -> HttpResponse:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(10))
    return HttpResponse(password)
