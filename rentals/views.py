
from django.http import HttpResponse
import secrets
import string

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")


def about(request):
    return HttpResponse("Welcome to CarsRental! We provide affordable and reliable car rental services for everyone.")



def generate_password(request):
    characters = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    password = ''.join(
        secrets.choice(characters)
        for i in range(10)
    )

    return HttpResponse(password)

