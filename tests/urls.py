try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path

from tests.views import (
    ContextView,
    PartialsView,
    MustacheCPView,
    DjangoCPView,
    AppTemplateView,
)

urlpatterns = [
    re_path('^context$', ContextView.as_view()),
    re_path('^partials$', PartialsView.as_view()),
    re_path('^mustachecp$', MustacheCPView.as_view()),
    re_path('^djangocp$', DjangoCPView.as_view()),
    re_path('^apptemplate$', AppTemplateView.as_view()),
]
