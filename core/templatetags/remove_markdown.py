from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def nomarkdown(value):
   return value.replace('#','')