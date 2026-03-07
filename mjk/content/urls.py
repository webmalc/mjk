from django.urls import path
from django.views.decorators.cache import cache_page

from .views import content_render

CACHE_TIMEOUT = 60 * 60 * 24 * 7 * 30  # 30 days


app_name = "content"
urlpatterns = [
    path("contacts/", content_render, {"slug": "contacts"}, name="contacts"),
    path("", view=cache_page(CACHE_TIMEOUT)(content_render), name="index"),
    path("<str:slug>/", view=cache_page(CACHE_TIMEOUT)(content_render), name="content"),
]
