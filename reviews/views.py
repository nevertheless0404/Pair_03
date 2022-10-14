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
            new = form.save(commit=False)
            new.grade = len(new.star)
            new.save()

            return redirect("reviews:detail", new.pk)

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


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewCreationForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", pk)
    else:
        form = ReviewCreationForm(instance=review)
    context = {
        "form": form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("reviews:index")
