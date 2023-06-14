from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PersianAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persian_admin'
    verbose_name = "بخش انتخاب فونت"


    def ready(self):
        from persian_admin.models import Font
        post_migrate.connect(Font.post_migrate_handler, sender=self)