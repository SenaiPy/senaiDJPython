from django.urls import path 
from .views import home #vai importar as função criadas em projeto/urls.py

urlpatterns = [
    path("", home),
]
