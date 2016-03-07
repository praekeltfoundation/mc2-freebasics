from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from freebasics import views


urlpatterns = patterns(
    '',
    url(
        r'^$',
        views.FreeBasicsHomepageView.as_view(),
        name='home'
    ),
    url(r'^', include('mc2.urls')),
    url(
        r'^add/$',
        views.FreeBasicsControllerCreateView.as_view(),
        name='freebasics_add'
    ),
    url(
        r'^(?P<controller_pk>\d+)/$',
        views.FreeBasicsControllerEditView.as_view(),
        name='freebasics_edit'),
    url(r'^templates/$', views.TemplateDataList.as_view(), name='templates_list'),
    url(r'^templates/(?P<pk>[0-9]+)/$', views.TemplateDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
