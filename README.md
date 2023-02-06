# django-mustache

A straightforward Mustache-powered template engine for Django, extracted from [wq.db] and updated to support the new [template backend] infrastructure in Django 1.8 and newer.  *django-mustache* facilitates [progressive enhancement] by allowing you to share the same templates between Django and an offline-capable JavaScript [web app].  Combined with a shared [URL structure], this approach ensures that each page in your site can be selectively rendered on the [server or on the client][templates] as needed.

A number of Pystache/Mustache backends for Django exist, though many are outdated.  Only this library provides all of the following:

 * Full integration with existing Django context processors like `django.template.context_processors.csrf` and `django.contrib.auth.context_processors.auth`.*
 * Full test suite
 * Installable via PyPI
 * Compatible with Django 1.8 and newer


> *[wq/app.js] provides client-side equivalents for these context variables.

[![Latest PyPI Release](https://img.shields.io/pypi/v/django-mustache.svg)](https://pypi.org/project/django-mustache)
[![Release Notes](https://img.shields.io/github/release/wq/django-mustache.svg)](https://github.com/wq/django-mustache/releases)
[![License](https://img.shields.io/pypi/l/django-mustache.svg)](https://github.com/wq/django-mustache/blob/master/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/wq/django-mustache.svg)](https://github.com/wq/django-mustache/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wq/django-mustache.svg)](https://github.com/wq/django-mustache/network)
[![GitHub Issues](https://img.shields.io/github/issues/wq/django-mustache.svg)](https://github.com/wq/django-mustache/issues)

[![Python Support](https://img.shields.io/pypi/pyversions/django-mustache.svg)](https://pypi.org/project/django-mustache)
[![Django Support](https://img.shields.io/pypi/djversions/django-mustache.svg)](https://pypi.org/project/django-mustache)

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
[template backend]: https://docs.djangoproject.com/en/1.10/topics/templates
[progressive enhancement]: https://wq.io/docs/website
[web app]: https://wq.io/docs/web-app
[URL structure]: https://wq.io/docs/url-structure
[templates]: https://wq.io/docs/templates
[wq/app.js]: https://wq.io/docs/app-js
