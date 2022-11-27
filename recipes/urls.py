from django.urls import path
from recipes.views import home, sobre, contato


urlpatterns = [
    path("", home),  # home do site
    path("sobre/", sobre),  # /sobre/
    path("contato/", contato)  # /contato/
]
