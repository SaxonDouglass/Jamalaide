from django import template

register = template.Library()

@register.inclusion_tag('blogs/article.html')
def news_item(article, heading="h2"):
    return { 'article': article, 'heading': heading }
