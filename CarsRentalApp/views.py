from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.")

def about(request):
    return HttpResponse("A simple paragraph about Car Rentals.")

# Create your views here.
