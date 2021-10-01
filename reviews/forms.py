from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review",)
        labels = {
            "review": "리뷰",
        }

    def save(self, *args, **kargs):
        review = super().save(commit=False)
        return review
