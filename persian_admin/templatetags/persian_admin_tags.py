import django
from django import template
from persian_admin.cache import get_cached_active_font, set_cached_active_font
from persian_admin.models import Font



register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag



@simple_tag(takes_context=True)
def get_persian_admin_font(context):
    font = get_cached_active_font()
    if not font:
        font = Font.get_active_font()
        set_cached_active_font(font)
    return font


