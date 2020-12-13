from django import template

register = template.Library()

@register.filter
def arrendonda(value, casas):
    return round(value, casas)