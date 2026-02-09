from django.urls import path
from .views import (
    content_render,
)

app_name = "content"
urlpatterns = [
    path("", view=content_render, name="index"),
    path("<str:slug>/", view=content_render, name="content"),
]
