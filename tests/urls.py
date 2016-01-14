from django.conf.urls import patterns, url

from tests.views import (
    ContextView,
    PartialsView,
    MustacheCPView,
    DjangoCPView,
)

urlpatterns = patterns(
    '',
    url('^context$', ContextView.as_view()),
    url('^partials$', PartialsView.as_view()),
    url('^mustachecp$', MustacheCPView.as_view()),
    url('^djangocp$', DjangoCPView.as_view()),
)
