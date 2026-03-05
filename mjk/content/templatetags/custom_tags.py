from django import template
from filer.models import Image

register = template.Library()


@register.simple_tag
def get_filer_image(image_id):
    try:
        return Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        return None
