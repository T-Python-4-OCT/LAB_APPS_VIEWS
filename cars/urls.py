from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('password/generate/', views.password_generator, name='password_generator'),
]
