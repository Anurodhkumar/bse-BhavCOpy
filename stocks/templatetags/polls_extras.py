from django import template
register = template.Library()
@register.filter
def split(value, key):
    return eval(value)
