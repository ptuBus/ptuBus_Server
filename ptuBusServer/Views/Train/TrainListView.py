from ptuBusServer.Serializers import TrainTimeTableSerializer
from ptuBusServer.Models import TrainTimeTableModel
from rest_framework import generics

class TrainListView(generics.ListAPIView):
    serializer_class = TrainTimeTableSerializer

    def get_queryset(self):
        queryset = TrainTimeTableModel.objects.all()

        runDay = self.request.query_params.get('runDay', None)
        endStationID = self.request.query_params.get('endStationID', None)
        trainClass = self.request.query_params.get('trainClass', None)
        arrivalTime = self.request.query_params.get('arrivalTime', None)

        if runDay and endStationID and trainClass and arrivalTime is not None:
            queryset = queryset.filter(runDay=runDay, endStationID=endStationID,
                                       trainClass=trainClass, arrivalTime__startswith=arrivalTime)
        elif runDay and endStationID and trainClass is not None:
            queryset = queryset.filter(runDay=runDay, endStationID=endStationID,
                                       trainClass=trainClass)
        elif runDay and endStationID and arrivalTime is not None:
            queryset = queryset.filter(runDay=runDay, endStationID=endStationID,
                                       arrivalTime__startswith=arrivalTime)
        elif runDay and endStationID is not None:
            queryset = queryset.filter(runDay=runDay, endStationID=endStationID)
        return queryset