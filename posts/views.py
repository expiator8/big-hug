from django.http import Http404
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, UpdateView, View
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.views.generic.edit import FormView
from requests.api import get
from users import mixins as user_mixins
from . import models, forms
from reviews import forms as review_forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Post
    paginate_by = 18
    paginate_orphans = 5
    ordering = "-created"
    context_object_name = "posts"


class PostDetail(View):

    """PostDetail Definition"""

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        post = models.Post.objects.get_or_none(pk=pk)
        if not post:
            raise Http404()
        form = review_forms.CreateReviewForm()
        return render(
            self.request, "posts/post_detail.html", {"post": post, "form": form}
        )


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        title = request.GET.get("title")

        filter_args = {}

        if title:

            filter_args["name__startswith"] = title

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            post_type = form.cleaned_data.get("post_type")

            if post_type is not None:
                filter_args["post_type"] = post_type

            qs = models.Post.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            posts = paginator.get_page(page)

            return render(
                request,
                "posts/search.html",
                {"title": title, "form": form, "posts": posts},
            )

        else:
            form = forms.SearchForm()

        return render(request, "posts/search.html", {"form": form})


class EditPostView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Post
    template_name = "posts/post_edit.html"
    fields = (
        "name",
        "post_type",
        "description",
    )

    success_message = "Post Updated"

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        if post.writer.pk != self.request.user.pk:
            raise Http404
        return post

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].label = "글 제목"
        form.fields["post_type"].label = "글 종류"
        form.fields["description"].label = "내용"
        return form


class CreatePostView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreatePostForm
    template_name = "posts/post_create.html"

    def form_valid(self, form):
        post = form.save()
        post.writer = self.request.user
        post.save()
        messages.success(self.request, "Post Created")
        return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))
