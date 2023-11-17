from django import template
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter("has_group")
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all() or user.is_staff or user.is_superuser


@register.filter("split")
def split(value, delimiter):
    return value.split(delimiter)


@register.filter("translate")
def translate(value):
    return _(value)
