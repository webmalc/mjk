from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ["slug", "title", "created_at", "updated_at"]
    search_fields = ["slug", "title", "content", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-updated_at"]
