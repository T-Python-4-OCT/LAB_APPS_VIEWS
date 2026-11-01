from django.shortcuts import render
import random
import string
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about(request):
    
    return HttpResponse("We are excited to have you here! Our car rental company is your perfect destination for reliable, comfortable, and affordable car rentals. We offer a wide selection of high-quality vehicles to meet your needs, with competitive prices and excellent customer service. Our goal is to provide every customer with a smooth and enjoyable rental experience. Your satisfaction is our top priority, and we are always happy to serve you! 🚗")


def password_generator(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return HttpResponse(f"Generated Password: {password}")