from django import template

register = template.Library()


@register.filter
def mediapath_filter(image):
    return '/media/' + str(image)
