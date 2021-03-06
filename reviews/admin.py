from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Review Admin Definition"""

    list_display = ("user", "__str__")

    search_fields = ("post__name",)
