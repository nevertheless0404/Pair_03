from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):

    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }

    return render(request, "accounts/signup.html", context)
