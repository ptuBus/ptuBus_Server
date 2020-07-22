from django.urls import re_path
from ptuBusServer.Views.Subway.SubwayListView import SubwayListView
from ptuBusServer.Views.Bus.BusListView import BusListView
from ptuBusServer.Views.schoolBus.schoolBusListView import SchoolBusListView
from ptuBusServer.Views.Train.TrainListView import TrainListView

urlpatterns = [
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)(&P<arrTime>\d)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<arrTime>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/$', SubwayListView.as_view()),
    re_path(r'^Bus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<schedule>\d+)/$', BusListView.as_view()),
    re_path(r'^Bus/(?P<startStationID>.+)(&P<endStationID>.+)/$', BusListView.as_view()),
    re_path(r'^Bus/$', BusListView.as_view()),
    re_path(r'^schoolBus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)(&P<arrTime>\d+)/$', SchoolBusListView.as_view()),
    re_path(r'^schoolBus/(?P<startStationID>.+)(&P<endStationID>.+)(&P<upDownTypeCode>.+)/$', SchoolBusListView.as_view()),
    re_path(r'^schoolBus/$', SchoolBusListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationName>[ㄱ-힣]+)(&P<trainClass>[1-3]+)(&P<arrivalTime>\d+)/$', TrainListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationName>[ㄱ-힣]+)(&P<trainClass>[1-3]+)/$', TrainListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationName>[ㄱ-힣]+)(&P<arrivalTime>\d)/$', TrainListView.as_view()),
    re_path(r'^train/(?P<runDay>.+)(&P<endStationName>[ㄱ-힣]+)/$', TrainListView.as_view()),
    re_path(r'^train/$', TrainListView.as_view()),
]