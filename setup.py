from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Mustache template engine for Django 1.8 and newer, with support for Django context processors.
"""


def readme():
    try:
        readme = open("README.md")
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


setup(
    name='django-mustache',
    use_scm_version=True,
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='https://github.com/wq/django-mustache',
    license='MIT',
    packages=['django_mustache'],
    description=LONG_DESCRIPTION.strip(),
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'Django>=1.8',
        'pystache',
    ],
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',

        'Topic :: Text Processing :: Markup :: HTML',
    ],
    test_suite='tests',
    tests_require=[
        'djangorestframework'
    ],
    setup_requires=[
        'setuptools_scm',
    ],
)
