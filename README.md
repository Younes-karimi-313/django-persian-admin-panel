# django-persian-admin-panel
django-persian-admin-panel is a Django app for fast and easy use of Persian fonts in the Django admin panel.
## Installation
- Run `pip install django-persian-admin-panel`
- Add `persian-admin` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    "persian-admin",
    #...
    "django.contrib.admin",
    #...
)

```
- Run `python manage.py migrate`
- Restart your application server
- Visit http://127.0.0.1:8000/admin/
