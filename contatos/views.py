from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http.request import HttpRequest
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Contato

# Create your views here.


def index(request: HttpRequest):

    contatos = Contato.objects.order_by("-id").filter(mostrar=True)
    paginator = Paginator(contatos, 1)
    page = request.GET.get("p")
    contatos = paginator.get_page(page)
    context = {}
    context["contatos"] = contatos
    return render(request=request, template_name="contatos/index.html", context=context)


def ver_contato(request: HttpRequest, contato_id: int):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, "contatos/ver_contato.html", {"contato": contato})


def busca(request: HttpRequest):
    termo = request.GET.get("termo")
    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR, "O campo busca não pode ser vazio"
        )
        return redirect("contatos:index")
    else:
        messages.add_message(request, messages.SUCCESS, "Contato encontrado")
    campos = Concat("nome", Value(""), "sobrenome")
    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True,
    )
    paginator = Paginator(contatos, 1)
    page = request.GET.get("p")
    contatos = paginator.get_page(page)
    context = {}
    context["contatos"] = contatos
    return render(request, "contatos/busca.html", context)
