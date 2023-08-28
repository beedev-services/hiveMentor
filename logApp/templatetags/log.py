from django import template

register = template.Library()

@register.filter(name='checkProfile')
def checkProfile():
    pass