from django.shortcuts import render, redirect
from .forms import ReviewCreationForm
from .models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.order_by("-id")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("reviews:index")

    else:
        form = ReviewCreationForm()

    context = {
        "form": form,
    }

    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)
