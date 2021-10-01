from django.db import models
from core import models as core_models
from django.shortcuts import reverse


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PostType(AbstractItem):

    """PostType Model Definition"""

    class Meta:
        verbose_name_plural = "Post Type"


class Post(core_models.TimeStampedModel):

    """Post Model Defenition"""

    name = models.CharField(max_length=140)
    writer = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    post_type = models.ForeignKey(
        "PostType", related_name="posts", on_delete=models.SET_NULL, null=True
    )
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
