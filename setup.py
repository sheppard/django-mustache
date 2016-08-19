import os
from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Mustache template engine for Django 1.8 and newer, with support for Django context processors.
"""


def parse_markdown_readme():
    """
    Convert README.md to RST via pandoc, and load into memory
    (fallback to LONG_DESCRIPTION on failure)
    """
    # Attempt to run pandoc on markdown file
    import subprocess
    try:
        subprocess.call(
            ['pandoc', '-t', 'rst', '-o', 'README.rst', 'README.md']
        )
    except OSError:
        return LONG_DESCRIPTION

    # Attempt to load output
    try:
        readme = open(os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ))
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


setup(
    name='django-mustache',
    version='1.0.0',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='https://github.com/wq/django-mustache',
    license='MIT',
    packages=['django_mustache'],
    description=LONG_DESCRIPTION.strip(),
    long_description=parse_markdown_readme(),
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
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    test_suite='tests',
    tests_require=[
        'djangorestframework'
    ],
)
