from django.urls import re_path, path
from .Views import *

urlpatterns = [
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)(&P<arrTime>\d)/$', SubwayTimeTableListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<arrTime>[0-1]+)/$', SubwayTimeTableListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)/$', SubwayTimeTableListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)/$', SubwayTimeTableListView.as_view()),
    re_path(r'^subway/$', SubwayTimeTableListView.as_view()),
    re_path(r'^bus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<schedule>\d+)/$', BusTimeTableListView.as_view()),
    re_path(r'^bus/(?P<startStationID>.+)(&P<endStationID>.+)/$', BusTimeTableListView.as_view()),
    re_path(r'^bus/$', BusTimeTableListView.as_view()),
    path('bus/terminal/', BusTerminalListView.as_view()),
    re_path(r'^schoolbus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)(&P<arrTime>\d+)/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^schoolbus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^schoolbus/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<trainClass>[1-3]+)(&P<arrivalTime>\d+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<trainClass>[1-3]+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<arrivalTime>\d)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/$', TrainTimeTableListView.as_view()),
    path('train/station/', TrainStationListView.as_view())
]