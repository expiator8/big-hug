from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
    path("", views.SearchView.as_view(), name="search"),
    path("<int:pk>", views.PostDetail.as_view(), name="detail"),
]
