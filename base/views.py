from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required

from base.forms import _UserCreationForm, StudentForm
from base.models import Student


def index(request):
    context = {"title": "Home"}

    return render(request, "index.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse("base:index"))

    context = {"title": "Login"}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse("base:index"))

    return render(request, "pages/login.html", context)


def register(request):
    context = {"title": "Register"}

    if request.method == "POST":
        form = _UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)

        context["form"] = form
        return render(request, "pages/register.html", context)

    form = _UserCreationForm()
    context["form"] = form

    return render(request, "pages/register.html", context)


def logout(request):
    auth_logout(request)

    return redirect(settings.LOGOUT_REDIRECT_URL)


@user_passes_test(lambda u: u.is_superuser)
def userDelete(request, pk):
    if pk != request.user.id:
        user = User.objects.get(id=pk)
        user.delete()

    return redirect("/dashboard")


@login_required()
def userUpdate(request, pk):
    context = {"title": "Update"}
    user = User.objects.get(id=pk)
    student = Student.objects.filter(user=user).first()
    form = None

    if request.method == "POST":
        if student is not None:
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.user = user
            student.save()
            return redirect(reverse("base:dashboard"))

        context["form"] = form
        return render(request, "pages/user_update.html", context)

    if student is not None:
        form = StudentForm(instance=student)
    else:
        form = StudentForm()

    context["form"] = form

    return render(request, "pages/user_update.html", context)


@login_required()
def dashboard(request):
    users = None

    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = User.objects.filter(id=request.user.id)

    context = {"title": "Dashboard", "users": users}

    return render(request, "pages/dashboard.html", context)
