from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.all()
    context = {}
    context["contatos"] = contatos
    return render(request=request, template_name="contatos/index.html", context=context)


def ver_contato(request: HttpRequest, contato_id: int):
    contato = Contato.objects.get(id=contato_id)
    return render(request, "contatos/ver_contato.html", {"contato": contato})
