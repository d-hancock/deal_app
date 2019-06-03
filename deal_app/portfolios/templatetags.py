import bleach
import json as jsonlib

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def json(value):
    uncleaned = jsonlib.dumps(value)
    clean = bleach.clean(uncleaned)

    try:
        jsonlib.loads(clean)
    except:
        raise ValueError('JSON contains a quote or escape sequence that was unable to be stripped')

    return mark_safe(clean)
