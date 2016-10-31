SECRET_KEY = '1234'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = "tests.urls"
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    'UNAUTHENTICATED_USER': None,
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'tests.test_app',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
]

context_processors = {
    'django.template.context_processors.csrf',
    'django.contrib.auth.context_processors.auth',
    'tests.context_processors.simple',
    'tests.context_processors.is_authenticated',
}

TEMPLATES = [
    {
        'BACKEND': 'django_mustache.Mustache',
        'DIRS': ['tests/mustache_templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': context_processors,
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['tests/django_templates'],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': context_processors,
        }
    }
]
