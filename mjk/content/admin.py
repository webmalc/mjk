from django.contrib import admin
from .models import Content, Feedback


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["slug", "title", "created_at", "updated_at"]
    search_fields = ["slug", "title", "content", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-updated_at"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active", "created_at", "updated_at"]
    search_fields = ["name", "phone", "email", "note"]
    ordering = ["-created_at"]
