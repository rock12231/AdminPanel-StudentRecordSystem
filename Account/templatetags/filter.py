from django import template

register = template.Library()

@register.filter(name='unique_data')
def unique_data(value):
    if value:
        return value[0].distinct()
