from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "posts.Post",
        related_name="reviews",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.review} - {self.post}"

    class Meta:
        ordering = ("-created",)
