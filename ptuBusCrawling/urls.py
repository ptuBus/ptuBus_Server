from django.urls import path
from ptuBusCrawling.Views import *

urlpatterns = [
    path('Subway/', SubwayListView.as_view()),
    path('subway/', SubwayListView.as_view()),
    path('SchoolBus/', SchoolBusListView.as_view()),
    path('schoolbus/', SchoolBusListView.as_view()),
    path('BusTerminal/', BusTerminalListView.as_view()),
    path('busterminal/', BusTerminalListView.as_view()),
    path('BusTimeTable/', BusTimeTableListView.as_view()),
    path('bustimetable/', BusTimeTableListView.as_view()),
    path('TrainStation/', TrainStationListView.as_view()),
    path('trainstation/', TrainStationListView.as_view()),
    path('TrainTimeTable/', TrainTimeTableListView.as_view()),
    path('traintimetable/', TrainTimeTableListView.as_view()),
]