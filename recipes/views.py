from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página Home")


def contato(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página contato")


def sobre(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Página sobre")
