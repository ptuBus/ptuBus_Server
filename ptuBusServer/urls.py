from django.urls import re_path, path
from .Views import *

urlpatterns = [
    path('subway/line/', SubwayLineListView.as_view()),
    path('subway/station/', SubwayStationListView.as_view()),
    re_path(r'^bus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<schedule>\d+)/$', BusTimeTableListView.as_view()),
    re_path(r'^bus/(?P<startStationID>.+)(&P<endStationID>.+)/$', BusTimeTableListView.as_view()),
    re_path(r'^bus/$', BusTimeTableListView.as_view()),
    path('bus/terminal/', BusTerminalListView.as_view()),
    re_path(r'^schoolbus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)(&P<schedule>\d+)/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^schoolbus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^schoolbus/$', SchoolBusTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<trainClass>[1-3]+)(&P<schedule>\d+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<trainClass>[1-3]+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)(&P<schedule>\d)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationID>.+)/$', TrainTimeTableListView.as_view()),
    re_path(r'^train/$', TrainTimeTableListView.as_view()),
    path('train/station/', TrainStationListView.as_view()),
    path('app/version', AppDBView.as_view()),
    path('app/download', FileDownloadListView.as_view())
]