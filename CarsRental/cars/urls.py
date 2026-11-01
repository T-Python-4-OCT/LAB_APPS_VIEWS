from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('password/generate/', views.password_generate, name='password_generate'),
]