from django.shortcuts import render

from .models import Contato

# Create your views here.


def index(request):
    contatos = Contato.objects.all()
    context = {}
    context["contatos"] = contatos
    return render(request=request, template_name="contatos/index.html", context=context)
