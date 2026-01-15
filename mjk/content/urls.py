from django.urls import path
from .views import (
    IndexView,
    AboutView,
    ServicesView,
    ServicesCleaningView,
    ServicesExploitationView,
    ServicesManagementView,
    ServicesSecurityView,
    ObjectsView,
    ContactsView,
    PrivacyPolicyView,
)

app_name = "content"
urlpatterns = [
    path("", view=IndexView.as_view(), name="index"),
    path("about/", view=AboutView.as_view(), name="about"),
    path("services/", view=ServicesView.as_view(), name="services"),
    path("services/cleaning/", view=ServicesCleaningView.as_view(), name="services_cleaning"),
    path("services/exploitation/", view=ServicesExploitationView.as_view(), name="services_exploitation"),
    path("services/management/", view=ServicesManagementView.as_view(), name="services_management"),
    path("services/security/", view=ServicesSecurityView.as_view(), name="services_security"),
    path("objects/", view=ObjectsView.as_view(), name="objects"),
    path("contacts/", view=ContactsView.as_view(), name="contacts"),
    path("privacy-policy/", view=PrivacyPolicyView.as_view(), name="privacy_policy"),
]