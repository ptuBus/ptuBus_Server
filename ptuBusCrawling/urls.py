from django.urls import path
from .Views.Subway.SubwayListView import SubwayListView
from .Views.SchoolBus.SchooBuslListView import SchooBuslListView
from .Views.Bus.BusTerminalListView import BusTerminalListView
from .Views.Bus.BusTimeTableListView import BusTimeTableListView

urlpatterns = [
    path('Subway/', SubwayListView.as_view()),
    path('SchoolBus/', SchooBuslListView.as_view()),
    path('BusTerminal/', BusTerminalListView.as_view()),
    path('BusTimeTable/', BusTimeTableListView.as_view()),
]