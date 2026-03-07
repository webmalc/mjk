from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import RequestContext
from django.template import Template
from django.utils.safestring import mark_safe

from .models import Content
from .models import Feedback
from .tasks import send_feedback_notification_email


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
