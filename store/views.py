from django.shortcuts import render, redirect


def home(request):
    return render(request, "store/home.html")


def register(request):
    return render(request, "store/register.html")


def login(request):
    return render(request, "store/login.html")


def dashboard(request):
    pass


def dealers(request):
    pass


def medicines(request):
    pass


def employees(request):
    pass


def customers(request):
    pass


def purchases(request):
    pass


def confirm_logout(request):
    return render(request, "store/confirm-logout.html")