from django.urls import re_path
from ptuBusServer.Views.Subway.SubwayListView import SubwayListView

urlpatterns = [
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)(&P<arrTime>\d)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<arrTime>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)(&P<isExpress>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/(?P<dailyTypeCode>[0-2]+)(&P<upDownTypeCode>[0-1]+)/$', SubwayListView.as_view()),
    re_path(r'^subway/$', SubwayListView.as_view())
]