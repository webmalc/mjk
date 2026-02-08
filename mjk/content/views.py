from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Content
from django.template import Template
from django.utils.safestring import mark_safe
from django.template import RequestContext


def content_render(request, slug="index"):
    if request.method == "POST" and slug == "contacts":
        pass
    content = get_object_or_404(Content, slug=slug)
    template = Template(content.content)
    context = RequestContext(request, {})
    rendered = template.render(context)
    return render(
        request,
        "content/content.html",
        {"content": content, "rendered": mark_safe(rendered)},
    )


class AboutView(TemplateView):
    template_name = "content/about.html"


class ServicesView(TemplateView):
    template_name = "content/services.html"


class ServicesCleaningView(TemplateView):
    template_name = "content/services_cleaning.html"


class ServicesExploitationView(TemplateView):
    template_name = "content/services_exploitation.html"


class ServicesManagementView(TemplateView):
    template_name = "content/services_management.html"


class ServicesSecurityView(TemplateView):
    template_name = "content/services_security.html"


class ObjectsView(TemplateView):
    template_name = "content/objects.html"


class ContactsView(TemplateView):
    template_name = "content/contacts.html"


class PrivacyPolicyView(TemplateView):
    template_name = "content/privacy_policy.html"
