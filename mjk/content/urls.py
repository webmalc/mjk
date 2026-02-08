from django.urls import path
from .views import (
    AboutView,
    ServicesView,
    ServicesCleaningView,
    ServicesExploitationView,
    ServicesManagementView,
    ServicesSecurityView,
    ObjectsView,
    PrivacyPolicyView,
    content_render,
)

app_name = "content"
urlpatterns = [
    path("", view=content_render, name="index"),
    path("<str:slug>/", view=content_render, name="content"),
    path("about/", view=AboutView.as_view(), name="about"),
    path("services/", view=ServicesView.as_view(), name="services"),
    path(
        "services/cleaning/",
        view=ServicesCleaningView.as_view(),
        name="services_cleaning",
    ),
    path(
        "services/exploitation/",
        view=ServicesExploitationView.as_view(),
        name="services_exploitation",
    ),
    path(
        "services/management/",
        view=ServicesManagementView.as_view(),
        name="services_management",
    ),
    path(
        "services/security/",
        view=ServicesSecurityView.as_view(),
        name="services_security",
    ),
    path("objects/", view=ObjectsView.as_view(), name="objects"),
    # path("contacts/", view=ContactsView.as_view(), name="contacts"),
    path("privacy-policy/", view=PrivacyPolicyView.as_view(), name="privacy_policy"),
]
