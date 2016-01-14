def simple(request):
    return {
        'simple': {
            'boolean': True,
            'list': [1, 2, 3],
        }
    }


def is_authenticated(request):
    return {
        'is_authenticated': request.user and request.user.is_authenticated()
    }
