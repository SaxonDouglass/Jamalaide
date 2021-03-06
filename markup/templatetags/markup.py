import markdown
import bleach

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def md(text):
    """processes markdown on the string"""
    extensions = ["nl2br", ]

    tags = bleach.ALLOWED_TAGS + ['br', 'cite', 'dd', 'dl', 'dt', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'p', 'pre', 'q', 'small', 'strike']
    attributes = bleach.ALLOWED_ATTRIBUTES
    attributes['img'] = ['src', 'alt']
    
    html = markdown.markdown(force_unicode(text), extensions)
    clean = bleach.clean(html, tags=tags, attributes=attributes)
    
    return mark_safe(clean)
