from ptuBusServer.Serializers import BusTimeTableSerializer
from ptuBusServer.Models import BusTimeTableModel
from rest_framework import generics
from rest_framework import status
from ..ptuBusErrorExcpetion import ptuBusErrorExcpetion


class BusTimeTableListView(generics.ListAPIView):
    serializer_class = BusTimeTableSerializer

    def get_queryset(self):
        queryset = BusTimeTableModel.objects.all()

        startStationID = self.request.query_params.get("startStationID", None)
        endStationID = self.request.query_params.get("endStationID", None)
        schedule = self.request.query_params.get("schedule", None)

        if startStationID and endStationID and schedule is not None:
            queryset = queryset.filter(
                startStationID=startStationID,
                endStationID=endStationID,
                schedule__startswith=schedule,
            )
        elif startStationID and endStationID is not None:
            queryset = queryset.filter(
                startStationID=startStationID,
                endStationID=endStationID,
            )
        if queryset:
            return queryset
        else:
            raise ptuBusErrorExcpetion(
                detail={
                    "error": "파라메터 값이 잘못되었습니다.",
                    "code": "-3",
                    "parameter": {
                        "startStationID": startStationID,
                        "endStationID": endStationID,
                        "schedule": schedule,
                    },
                },
                status_code=status.HTTP_400_BAD_REQUEST,
            )
