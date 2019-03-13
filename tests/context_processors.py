def simple(request):
    return {
        'simple': {
            'boolean': True,
            'list': [1, 2, 3],
        }
    }


def is_authenticated(request):
    is_authenticated = request.user and request.user.is_authenticated
    if callable(is_authenticated):
        is_authenticated = is_authenticated()

    return {
        'is_authenticated': is_authenticated,
    }
