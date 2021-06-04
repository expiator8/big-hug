from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    posts = models.ManyToManyField("posts.Post", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_posts(self):
        return self.posts.count()

    count_posts.short_description = "Number of Posts"
