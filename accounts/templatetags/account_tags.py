from django import template

from accounts.models import CommitteeMember, ContactLink

register = template.Library()

@register.inclusion_tag('accounts/committee_members.html')
def committee_members():
    return { 'executive': CommitteeMember.objects.exclude(title=""), 'general': CommitteeMember.objects.filter(title="") }

@register.inclusion_tag('accounts/contact_links.html')
def contact_links():
    return { 'links': ContactLink.objects.all() }
