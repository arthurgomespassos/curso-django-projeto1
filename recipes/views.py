from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    # já busca direto dentro da pasta templates se houver então
    # não precisa do caminho completo
    return render(request, 'recipes/home.html')


def contato(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página contato")


def sobre(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página sobre")
