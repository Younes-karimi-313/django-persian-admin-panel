# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.cache import cache, caches


def app_cache():
    return caches["persian_admin"] if "persian_admin" in settings.CACHES else cache


def del_cached_active_font():
    app_cache().delete("persian_admin_font")


def get_cached_active_font():
    return app_cache().get("persian_admin_font", None)


def set_cached_active_font(font):
    app_cache().set("persian_admin_font", font)
