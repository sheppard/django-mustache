# django-mustache

A straightforward Mustache-powered template engine for Django.  Extracted from [wq.db] and updated to support the new [template backend] infrastructure in Django 1.8 and newer.

A number of Pystache/Mustache backends for Django exist, though many are outdated.  Only this library provides all of the following:

 * Full integration with existing Django context processors like `django.template.context_processors.csrf` and `django.contrib.auth.context_processors.auth`.
 * Full test suite
 * Installable via PyPI
 * Compatible with Django 1.8 and newer

### Usage

```bash
pip3 install django-mustache
```

Configure django-mustache like you would any [template backend]:

```python
# myproject/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django_mustache.Mustache',
        'DIRS': [ '...' ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [ '...' ],
            'partials_dir': 'partials',
            'file_extension': 'html',
        }
    },
    # ...
]
```

The following configuration options are supported:

 * **context_processors**: equivalent to the Django template backend setting.  The goal is to be able to use the same context processors for both Django and Mustache template backends.  (Let us know if you come across any compatibility issues.)
 * **partials_dir**: If set, django-mustache will check each template directory for a subfolder containing Mustache partial templates.  The default partial folder name is 'partials'.  Set to `False` to disable this feature.
 * **file_extension**: File extension to use when searching for templates and partials.  The default is '.html', which should not conflict with existing Django templates as long as completely separate directories are configured for Mustache templates.  Django views typically include the extension in the template name - this is taken into account when searching for templates.

[wq.db]: https://wq.io/wq.db/
[template backend]: https://docs.djangoproject.com/en/1.9/topics/templates
