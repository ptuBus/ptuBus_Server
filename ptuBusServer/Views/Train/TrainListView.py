# -*- coding: utf-8 -*-
from ptuBusServer.Serializers import TrainTimeTableSerializer
from ptuBusServer.Models import TrainTimeTableModel
from rest_framework import generics
import urllib.parse

class TrainListView(generics.ListAPIView):
    serializer_class = TrainTimeTableSerializer

    def get_queryset(self):
        queryset = TrainTimeTableModel.objects.all()

        runDay = self.request.query_params.get('dailyTypeCode', None)
        endStationName = self.request.query_params.get('endStationName', None)
        endStationName = urllib.parse.unquote(endStationName)
        trainClass = self.request.query_params.get('trainClass', None)
        arrivalTime = self.request.query_params.get('arrivalTime', None)

        if runDay and endStationName and trainClass and arrivalTime is not None:
            queryset = queryset.Charfilter(runDay=runDay, endStationName=endStationName,
                                       trainClass=trainClass, arrivalTime__startswith=arrivalTime)
        elif runDay and endStationName and trainClass is not None:
            queryset = queryset.filter(runDay=runDay, endStationName=endStationName,
                                       trainClass=trainClass)
        elif runDay and endStationName and arrivalTime is not None:

            queryset = queryset.filter(runDay=runDay, endStationName=endStationName,
                                       arrivalTime__startswith=arrivalTime)
        elif runDay and endStationName is not None:
            queryset = queryset.filter(runDay=runDay, endStationName__=endStationName)
        return queryset