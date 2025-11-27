from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
a = 'SENAI' #variável

def home(request): #criando a URL home
    return render(request, "home.html", context=
                  {
                      'nome': a,
                  }
                  )

