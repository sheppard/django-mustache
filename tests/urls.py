from django.conf.urls import url

from tests.views import (
    ContextView,
    PartialsView,
    MustacheCPView,
    DjangoCPView,
    AppTemplateView,
)

urlpatterns = [
    url('^context$', ContextView.as_view()),
    url('^partials$', PartialsView.as_view()),
    url('^mustachecp$', MustacheCPView.as_view()),
    url('^djangocp$', DjangoCPView.as_view()),
    url('^apptemplate$', AppTemplateView.as_view()),
]
