from django import forms
from . import models


class SearchForm(forms.Form):

    post_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.PostType.objects.all()
    )

    # city = forms.CharField(initial="Anywhere")
    # country = CountryField(default="KR").formfield()
    # room_type = forms.ModelChoiceField(
    #     required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    # )
    # price = forms.IntegerField(required=False)
    # guests = forms.IntegerField(required=False)
    # bedrooms = forms.IntegerField(required=False)
    # beds = forms.IntegerField(required=False)
    # baths = forms.IntegerField(required=False)
    # instant_book = forms.BooleanField(required=False)
    # superhost = forms.BooleanField(required=False)
    # amenities = forms.ModelMultipleChoiceField(
    #     required=False,
    #     queryset=models.Amenity.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )
    # facilities = forms.ModelMultipleChoiceField(
    #     required=False,
    #     queryset=models.Facility.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "name",
            "post_type",
            "description",
        )
        labels = {
            "name": "글 제목",
            "post_type": "글 종류",
            "description": "내용",
        }

    def save(self, *args, **kargs):
        post = super().save(commit=False)
        return post
