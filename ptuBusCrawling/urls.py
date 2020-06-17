from django.urls import path
from . import views

urlpatterns = [
    path('Subway/', views.SubwayListView.as_view()),
    path('SchoolBus/', views.SchooBuslListView.as_view()),
    # path('BusTerminal/', views.BusTerminalListView.as_view()),
    # TypeError : string indices must be integers
    # .../ptuBusCrawling/views.py in get, line 73
    path('BusTimeTable/', views.BusTimeTableListView.as_view()),
]