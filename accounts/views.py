from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http.request import HttpRequest
from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    if request.method != "POST":

        return render(request, "accounts/login.html")
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")
    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, "usuario ou senha invalidos")
        return render(request, "accounts/login.html")

    auth.login(request, user)
    messages.success(request, "Logado com sucesso")
    return redirect("accounts:dashboard")


def register(request: HttpRequest):

    if request.method != "POST":
        return render(request, "accounts/register.html")

    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    email = request.POST.get("email")
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")
    senha2 = request.POST.get("repetirSenha")

    for field in request.POST.values():
        if not field:
            messages.error(request, "Nenhum campo pode ser vazio")
            return render(request, "accounts/register.html")
    try:
        validate_email(email)
    except:
        messages.error(request, "Email invalido")
        return render(request, "accounts/register.html")

    if len(senha) < 6:
        messages.error(request, "Senha muito pequena")
        return render(request, "accounts/register.html")
    if len(usuario) < 6:
        messages.error(request, "Nome do Usuario muito pequeno")
        return render(request, "accounts/register.html")
    print(senha, senha2)
    if senha != senha2:
        messages.error(request, "senhas sao diferentes")
        return render(request, "accounts/register.html")
    # if not senha:
    #     messages.error(request, "Nenhum campo pode ser vazio")
    #     return render(request, "accounts/register.html")
    if User.objects.filter(username=usuario):
        messages.error(request, "Usuario ja existe")
        return render(request, "accounts/register.html")
    if User.objects.filter(email=email):
        messages.error(request, "email ja existe")
        return render(request, "accounts/register.html")

    messages.success(request, "email criado com sucesso")
    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome,
    )
    user.save()
    return redirect("accounts:login")


def logout(request):
    auth.logout(request)
    return redirect("accounts:dashboard")


@login_required(redirect_field_name="accounts:login")
def dashboard(request):
    return render(request, "accounts/dashboard.html")


# def index(request):
#     return render(request, "accounts/index.html")
