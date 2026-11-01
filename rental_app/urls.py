from django.urls import path

from .views import about, home, password_generator

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('password/generate/', password_generator, name='password_generator'),
]
