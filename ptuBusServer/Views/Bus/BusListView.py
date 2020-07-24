from ptuBusServer.Serializers import BusTimeTableSerializer
from ptuBusServer.Models import BusTimeTableModel
from rest_framework import generics

class BusListView(generics.ListAPIView):
    serializer_class = BusTimeTableSerializer

    def get_queryset(self):
        queryset = BusTimeTableModel.objects.all()

        startStationID = self.request.query_params.get('startStationID', None)
        endStationID = self.request.query_params.get('endStationID', None)
        schedule = self.request.query_params.get('schedule', None)

        if startStationID and endStationID and schedule is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID=endStationID, schedule__startswith=schedule)
        elif startStationID and endStationID is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID__startswith=endStationID)
        return queryset