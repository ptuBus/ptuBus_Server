from django.urls import path
from .Views.Subway.SubwayListView import SubwayListView
from .Views.SchoolBus.SchoolBusListView import SchoolBusListView
from .Views.Bus.BusTerminalListView import BusTerminalListView
from .Views.Bus.BusTimeTableListView import BusTimeTableListView
from .Views.Train.TrainStationListView import TrainStationListView
from .Views.Train.TrainTimeTableListView import TrainTimeTableListView

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