from rest_framework.views import APIView
from rest_framework.response import Response


class View(APIView):
    context = {}

    @property
    def template_name(self):
        return "test_%s.html" % type(self).__name__.lower().replace('view', '')

    def get(self, request, *args, **kwargs):
        return Response(self.context)


class ContextView(View):
    context = {
        'test': 1234,
        'boolean': True,
        'none': None,
        'false': False,
        'nested': {
            'value': 5678,
        },
        'array': [1, 2, 3],
        'empty': [],
    }


class PartialsView(View):
    pass


class MustacheCPView(View):
    pass


class DjangoCPView(View):
    pass


class AppTemplateView(View):
    pass
