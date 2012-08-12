from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def gfm_markdown(value):
  """processes markdown on the string"""
  return markdown.markdown(markdown.gfm(value))
