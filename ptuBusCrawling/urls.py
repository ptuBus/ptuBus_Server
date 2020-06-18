from django.urls import path
from .Views.Subway.SubwayListView import SubwayListView
from .Views.SchoolBus.SchooBuslListView import SchooBuslListView
from .Views.Bus.BusTerminalListView import BusTerminalListView
from .Views.Bus.BusTimeTableListView import BusTimeTableListView
from .Views.Train.TrainStationListView import TrainStationListView
from .Views.Train.TrainTimeTableListView import TrainTimeTableListView

urlpatterns = [
    path('Subway/', SubwayListView.as_view()),
    path('SchoolBus/', SchooBuslListView.as_view()),
    path('BusTerminal/', BusTerminalListView.as_view()),
    path('BusTimeTable/', BusTimeTableListView.as_view()),
    path('TrainStation/', TrainStationListView.as_view()),
    path('TrainTimeTable/', TrainTimeTableListView.as_view()),
]