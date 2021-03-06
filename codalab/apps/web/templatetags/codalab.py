import os
from django import template

register = template.Library()


@register.filter
def filename(value):
    return os.path.basename(value.file.name)

# by mikeivanov (on April 16, 2007)


@register.filter
def in_list(value, arg):
    return value in arg

@register.filter
def get_type(value):
    if hasattr(value, '_type'):
        if value._type is not None:
            value._type = ContentType.objects.get_for_model(value)
    else:
        value._type = value.__class__.__name__
    return value._type