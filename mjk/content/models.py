from django.db import models
from tinymce import models as tinymce_models

# Create your models here.


class Content(models.Model):
    slug = models.SlugField(
        db_index=True,
        unique=True,
        verbose_name="URL",
    )
    content = tinymce_models.HTMLField(verbose_name="контент")
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="описание",
    )
    keywords = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="ключевые слова",
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="заголовок",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата обновления",
    )

    class Meta:
        verbose_name = "контент"
        verbose_name_plural = "контент"

    def __str__(self):
        return self.slug
