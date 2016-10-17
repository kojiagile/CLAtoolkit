
from django.conf.urls import patterns, url, include
from django.contrib import admin

import views

urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^myunits/$', views.myunits, name='myunits'),
    url(r'^ca_dashboard/$', views.cadashboard, name='cadashboard'),
    url(r'^sna_dashboard/$', views.snadashboard, name='snadashboard'),
    url(r'^student_dashboard/$', views.studentdashboard, name='studentdashboard'),
    url(r'^mydashboard/$', views.mydashboard, name='mydashboard'),
    url(r'^pyldavis/$', views.pyldavis, name='pyldavis'),
    url(r'^myclassifications/$', views.myclassifications, name='myclassifications'),
    url(r'^ccadashboard/$', views.ccadashboard, name='ccadashboard'),
    url(r'^ccadata/$', views.ccadata, name='ccadata'),
    url(r'^getBoards/$', views.get_trello_boards, name='gettrelloboards'),
    url(r'^addBoardToCourse/$', views.add_board_to_course, name='addboardtocourse'),
    url(r'^removeBoard/$', views.trello_remove_board, name='removetrelloboard'),
    #REST
    url(r'^getAttachedBoard/$', views.trello_myunits_restview, name='gettrellodashboardlink'),
    url(r'^api/get_platform_timeseries_data/$', views.get_platform_timeseries_data, name='get_platform_timeseries_data'),
    url(r'^api/get_platform_activities/$', views.get_platform_activities, name='get_platform_activities'),
)
