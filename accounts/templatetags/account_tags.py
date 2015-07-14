from django import template

from accounts.models import CommitteeMember

register = template.Library()

@register.inclusion_tag('accounts/committee_members.html')
def committee_members():
    return { 'executive': CommitteeMember.objects.exclude(title=""), 'general': CommitteeMember.objects.filter(title="") }
