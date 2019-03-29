from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter(name='cut')
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
