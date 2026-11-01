from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('password/generate/', views.password_generate_view, name='password_generate'),
]
