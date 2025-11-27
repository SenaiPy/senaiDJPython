from django.urls import path 
from .views import home, sobre, receita #vai importar as função criadas em projeto/urls.py

urlpatterns = [
    path("", home),
    path("sobre/", sobre),
    path("receitas/", receita),
]
