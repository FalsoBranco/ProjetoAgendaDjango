from django.core.paginator import Paginator
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Contato

# Create your views here.


def index(request: HttpRequest):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 1)
    page = request.GET.get("p")
    contatos = paginator.get_page(page)
    context = {}
    context["contatos"] = contatos
    return render(request=request, template_name="contatos/index.html", context=context)


def ver_contato(request: HttpRequest, contato_id: int):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, "contatos/ver_contato.html", {"contato": contato})
