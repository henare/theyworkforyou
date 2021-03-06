from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

import views
import models

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),

    url(r'^survey$', views.survey_candidacy),
    url(r'^survey/autosave/(?P<token>.+)$', views.survey_autosave),
    url(r'^survey/(?P<token>.+)$', views.survey_candidacy),

    url(r'^survey/$', redirect_to, {'url' : '/survey'} ),

    url(r'^quiz$', views.quiz_index),

    url(r'^admin/?$', redirect_to, {'url' : '/admin/index'} ),
    url(r'^admin/index$', views.admin_index),
    url(r'^admin/stats$', views.admin_stats),
    url(r'^admin/responses$', views.admin_responses),

    url(r'^task/invite_candidacy_survey/(?P<candidacy_key_name>[\d-]+)$', views.task_invite_candidacy_survey),

    # url(r'^fooble$', views.fooble),

    # Example:
    # (r'^electionsurvey/', include('electionsurvey.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
