from ptuBusServer.Serializers import SchoolBusTimeTableSerializer
from ptuBusServer.Models import SchoolBusTimeTableModel
from rest_framework import generics

class SchoolBusTimeTableListView(generics.ListAPIView):
    serializer_class = SchoolBusTimeTableSerializer

    def get_queryset(self):
        queryset = SchoolBusTimeTableModel.objects.all()

        startStationID = self.request.query_params.get('startStationID', None)
        endStationID = self.request.query_params.get('endStationID', None)
        upDownTypeCode = self.request.query_params.get('upDownTypeCode', None)
        arrTime = self.request.query_params.get('arrTime', None)

        if startStationID and endStationID and upDownTypeCode and arrTime is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID=endStationID,
                                       upDownTypeCode=upDownTypeCode, arrTime__startswith=arrTime)
        elif startStationID and endStationID and upDownTypeCode is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID=endStationID,
                                       upDownTypeCode=upDownTypeCode)

        return queryset