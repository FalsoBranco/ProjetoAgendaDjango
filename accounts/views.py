from django.contrib import messages
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "accounts/login.html")


def register(request):
    messages.add_message(request, messages.ERROR, "")
    return render(request, "accounts/register.html")


def logout(request):
    return render(request, "accounts/logout.html")


def dashboard(request):
    return render(request, "accounts/dashboard.html")


# def index(request):
#     return render(request, "accounts/index.html")
