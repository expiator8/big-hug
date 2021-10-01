from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("users/", include("users.urls", namespace="users")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("conversations/", include("conversations.urls", namespace="conversations")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
