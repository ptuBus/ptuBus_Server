from django.urls import path
from . import views

urlpatterns = [
    path('Subway/', views.SubwayListView.as_view()),
    # path('schoolbus/', views.SchoolListView.as_view()),
]