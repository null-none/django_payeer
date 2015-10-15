from django.conf.urls import patterns, url
from .views import *
from . import NAME
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^' + settings.PAYEER_RESULT_URL + '/$', deposit_result, name='deposit_result_' + NAME),
)