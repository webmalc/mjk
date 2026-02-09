from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from .models import Content, Feedback
from django.template import Template
from django.utils.safestring import mark_safe
from django.template import RequestContext
from .tasks import send_feedback_notification_email

CACHE_TIMEOUT = 60 * 60 * 24 * 7 * 30  # 30 days


@cache_page(CACHE_TIMEOUT)
def content_render(request, slug="index"):
    if request.method == "POST" and slug == "contacts":
        return add_feedback(request)
    content = get_object_or_404(Content, slug=slug)
    template = Template(content.content)
    context = RequestContext(request, {})
    rendered = template.render(context)
    return render(
        request,
        "content/content.html",
        {"content": content, "rendered": mark_safe(rendered)},
    )


def add_feedback(request):
    name = request.POST.get("name", "")
    phone = request.POST.get("tel", "")
    email = request.POST.get("email", "")
    note = request.POST.get("text", "")

    if not phone:
        return redirect("content:content", slug="contacts")

    Feedback.objects.create(
        name=name,
        phone=phone,
        email=email,
        note=note,
    )
    send_feedback_notification_email.delay(name, phone, email, note)
    response = redirect("content:content", slug="contacts")
    response["Location"] += "?success=1"
    return response
