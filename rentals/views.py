from django.http import HttpResponse
import random
import string
# Create your views here.
def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.")

def about(request):
    return HttpResponse("Car Rentals offers a simple and convenient way to rent a car for your daily trips and travels.")

def generate_password(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))

    return HttpResponse(password)