from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task()
def send_feedback_notification_email(name, phone, email, note):
    """Send email notification to managers about new feedback."""
    managers_emails = [manager[1] for manager in settings.MANAGERS]

    subject = "Новое сообщение обратной связи"
    message = f"""Получено новое сообщение обратной связи:
Имя: {name}
Телефон: {phone}
Email: {email or "не указан"}
Сообщение: {note or "не указано"}
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL or settings.SERVER_EMAIL,
        recipient_list=managers_emails,
        fail_silently=True,
    )
