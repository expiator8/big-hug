from django.http import request
from django.views.generic import FormView, View
from django.shortcuts import redirect, reverse
from posts import models as post_models
from users import mixins as user_mixins
from . import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def create_review(request, post):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        post = post_models.Post.objects.get_or_none(pk=post)
        if not post:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.post = post
            review.user = request.user
            review.save()
            messages.success(request, "Post reviewed")
            return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))
