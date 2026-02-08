from django.db import models

# Create your models here.


class Content(models.Model):
    slug = models.SlugField(
        db_index=True,
        unique=True,
        verbose_name="URL",
    )
    content = models.TextField(
        verbose_name="контент",
    )
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


class Feedback(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="имя",
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="телефон",
    )
    email = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="e-mail",
    )
    note = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="комметарий",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата обновления",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Обрабатана?",
    )

    class Meta:
        verbose_name = "обратная связь"
        verbose_name_plural = "обратная связь"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"Обратная связь {self.phone} {self.created_at.strftime('%d.%m.%Y %H:%M')}"
        )
