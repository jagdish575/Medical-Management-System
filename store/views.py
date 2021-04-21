from django.shortcuts import render, redirect
from .forms import CreateUserForm, LogUserForm

def home(request):
    return render(request, "store/home.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("store:login")
        return redirect("store:register")

    context = {
        "form": form
    }
    return render(request, "store/register.html", context)


def login(request):
    form = LogUserForm()

    context = {
        "form": form
    }
    return render(request, "store/login.html", context)


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