from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Content
from django.template import Template
from django.utils.safestring import mark_safe
from django.template import RequestContext

CACHE_TIMEOUT = 60 * 60 * 24 * 7 * 30  # 30 days


@cache_page(CACHE_TIMEOUT)
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


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class AboutView(TemplateView):
    template_name = "content/about.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ServicesView(TemplateView):
    template_name = "content/services.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ServicesCleaningView(TemplateView):
    template_name = "content/services_cleaning.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ServicesExploitationView(TemplateView):
    template_name = "content/services_exploitation.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ServicesManagementView(TemplateView):
    template_name = "content/services_management.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ServicesSecurityView(TemplateView):
    template_name = "content/services_security.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class ObjectsView(TemplateView):
    template_name = "content/objects.html"


class ContactsView(TemplateView):
    template_name = "content/contacts.html"


@method_decorator(cache_page(CACHE_TIMEOUT), name="get")
class PrivacyPolicyView(TemplateView):
    template_name = "content/privacy_policy.html"
