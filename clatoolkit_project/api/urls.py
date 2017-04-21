__author__ = 'Koji'

from analytics.views import TimeseriesRequest
from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter


urlpatterns = patterns('',
	# Analytics API
	url(r'^unit/(?P<unit_id>[a-zA-Z0-9]+)/timeseries/platforms/$', 
		TimeseriesRequest.as_view(), {'type': TimeseriesRequest.TIMESERIES_DATATYPE_PLATFORM}, name='PlatformTimeseries'),
	url(r'^unit/(?P<unit_id>[a-zA-Z0-9]+)/timeseries/verbs/$', 
		TimeseriesRequest.as_view(), {'type': TimeseriesRequest.TIMESERIES_DATATYPE_VERB}, name='VerbTimeseries'),
)

