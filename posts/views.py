from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Post
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "posts"


class PostDetail(DetailView):

    """PostDetail Definition"""

    model = models.Post


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        title = request.GET.get("title")

        filter_args = {}

        if title is not None:
            filter_args["name__startswith"] = title

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            post_type = form.cleaned_data.get("post_type")

            if post_type:
                filter_args["post_type"] = post_type

            qs = models.Post.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            posts = paginator.get_page(page)

            return render(request, "posts/search.html", {"form": form, "posts": posts})

        else:
            form = forms.SearchForm()

        return render(request, "posts/search.html", {"form": form})
