from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
a = 'Receitas Django' #variável

def home(request): #criando a URL home
    return render(request, "home.html", context=
                  {
                      'nome': a,
                  }
                  )

def sobre(request): #criando a URL sobre
    return HttpResponse("Sobre nós")

def receita(request): #criando a URL receita
    return HttpResponse("As receitas")

def senai(request): #criando a URL senai
    return HttpResponse("Olá, Senai!")

