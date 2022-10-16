from cProfile import label
from django.forms import ModelForm
from .models import Review


class ReviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "title": "제목",
            "content": "내용",
            "movie_name": "영화 이름",
            "grade": "영화 평점",
        }
