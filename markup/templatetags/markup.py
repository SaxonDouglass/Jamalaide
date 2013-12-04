import markdown

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

    return mark_safe(markdown.markdown(force_unicode(text),
                                        extensions,
                                        safe_mode=True,
                                        enable_attributes=False))
