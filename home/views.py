from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

# Create your views here.


def index(request):
    if request.method == "POST":
        home = Home()
        home.recipe_name = request.POST.get("recipe_name")
        home.recipe_description = request.POST.get("recipe_description")
        home.recipe_image = request.FILES.get("recipe_image")
        home.save()

        return redirect("/")

    queryset = Home.objects.all()

    if request.GET.get("recipe_search"):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get("recipe_search")
        )

    context = {
        "title": "Savorify",
        "year": datetime.datetime.now().year,
        "recipes": queryset,
    }

    return render(request, "index.html", context)


def update_recipe(request, id):
    recipe = Home.objects.get(id=id)
    context = {
        "title": "Savorify",
        "year": datetime.datetime.now().year,
        "recipe": recipe,
    }

    if request.method == "POST":
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")

        if request.FILES.get("recipe_image"):
            recipe.recipe_image = request.FILES.get("recipe_image")

        recipe.save()
        return redirect("/")

    return render(request, "update_recipe.html", context)


def delete_recipe(request, id):
    recipe = Home.objects.get(id=id)
    recipe.delete()
    return redirect("/")


def login_page(request):
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already exists")
            return redirect("/register")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Registered Successfully")
        return redirect("/register")

    return render(request, "register.html")
