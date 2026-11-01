
import secrets
import string
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    contact = "Hello World, This is my new HOME page for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(contact)

def about_view(request):
    contact = "Welcome to CarsRental! We make renting a car easy, affordable, and convenient. Whether you need a car for a vacation, a business trip, or everyday use, we offer a variety of vehicles to suit your needs. Our goal is to provide reliable cars, competitive prices, and excellent customer service to make your rental experience as smooth as possible."
    return HttpResponse(contact)

def password_view(request):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        contact = "".join(secrets.choice(characters) for _ in range(10))
        if (any(char.islower() for char in contact)
                and any(char.isupper() for char in contact)
                and any(char.isdigit() for char in contact)
                and any(char in string.punctuation for char in contact)):
            break
    return HttpResponse(contact)
