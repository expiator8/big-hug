from django.contrib import admin
from . import models


@admin.register(models.PostType)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.posts.count()


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    list_display = (
        "name",
        "writer",
        "post_type",
    )

    ordering = (
        "name",
        "writer",
        "post_type",
    )

    list_filter = ("post_type",)

    raw_id_fields = ("writer",)

    search_fields = ("writer",)
