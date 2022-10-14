from django.forms import ModelForm
from .models import Review

class ReviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"