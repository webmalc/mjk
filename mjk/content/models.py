from django.db import models

# Create your models here.


class Content(models.Model):
    slug = models.SlugField(
        db_index=True,
    )
    content = models.TextField()
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    keywords = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.slug
