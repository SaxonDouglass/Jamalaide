from django import template
from django.template.defaultfilters import stringfilter
import jamalaide.markdown

register = template.Library()

@register.filter
@stringfilter
def gfm_markdown(value):
  """processes markdown on the string"""
  return jamalaide.markdown.markdown(value)
