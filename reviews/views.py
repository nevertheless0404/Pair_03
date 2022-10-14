from django.shortcuts import render, redirect
from .forms import ReviewCreationForm
from .models import Review

# Create your views here.

def index(request):
    return render(request, "reviews/index.html")


def create(request):
    if request.method == "POST":
        form = ReviewCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("reviews:index")

    else:
        form = ReviewCreationForm()

    context = {
        'form': form,
    }

    return render(request, "reviews/create.html", context)