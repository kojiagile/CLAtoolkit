__author__ = 'Koji'

import json

from collections import OrderedDict
from django.http import HttpResponse, JsonResponse
from endpoint.timeseries import Timeseries
from validator.timeseries_validator import TimeseriesValidator

from rest_framework import authentication, permissions, viewsets, filters
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..error.application_error import ApplicationError
from ..error.invalid_parameter_error import InvalidParameterError


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.SessionAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 300
    paginate_by_param = 'page_size'
    max_paginate_by = 1000

    filter_backends = (
        filters.SearchFilter,
        filters.DjangoFilterBackend,
        filters.OrderingFilter
    )


class TimeseriesRequest(DefaultsMixin, APIView):
	TIMESERIES_DATATYPE_PLATFORM = 'platform'
	TIMESERIES_DATATYPE_VERB = 'verb'

	# https://docs.djangoproject.com/en/1.10/ref/class-based-views/base/#django.views.generic.base.View.as_view
	def get(self, request, *args, **kw):
		resp = None
		try:
			TimeseriesValidator.valid_timeseries_params(request, args, kw)

			if kw['type'] == self.TIMESERIES_DATATYPE_PLATFORM:
				resp = Timeseries.get_platform_timeseries(request, args, kw)

			elif kw['type'] == self.TIMESERIES_DATATYPE_VERB:
				resp = Timeseries.get_verb_timeseries(request, args, kw)

		except InvalidParameterError as ipexp:
			ipexp.print_errorlog_message()
			resp = {'status': 'error', 'message': '%s' % (ipexp.message)}

		except ApplicationError as appexp:
			appexp.print_errorlog_message()
			resp = {'status': 'error', 'message': '%s' % (appexp.message)}

		return JsonResponse(resp, status=status.HTTP_200_OK)

