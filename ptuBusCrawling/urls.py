from django.urls import path
from ptuBusCrawling.Views import *

urlpatterns = [
    path('schoolbus/', SchoolBusListView.as_view()),
    path('busterminal/', BusTerminalListView.as_view()),
    path('bustimetable/', BusTimeTableListView.as_view()),
    path('trainstation/', TrainStationListView.as_view()),
    path('traintimetable/', TrainTimeTableListView.as_view()),
    path('sqlite/', sqliteView.as_view()),

]