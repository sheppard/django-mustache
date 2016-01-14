if [ "$LINT" ]; then
    flake8 django_mustache tests
else
    python setup.py test
fi
