from ptuBusServer.Serializers import TrainTimeTableSerializer
from ptuBusServer.Models import TrainTimeTableModel
from rest_framework import generics
from rest_framework import status
from ..ptuBusErrorExcpetion import ptuBusErrorExcpetion

class TrainTimeTableListView(generics.ListAPIView):
    serializer_class = TrainTimeTableSerializer

    def get_queryset(self):
        queryset = TrainTimeTableModel.objects.all()

        dailyTypeCode = self.request.query_params.get('dailyTypeCode', None)
        endStationID = self.request.query_params.get('endStationID', None)
        trainClass = self.request.query_params.get('trainClass', None)
        schedule = self.request.query_params.get('schedule', None)
        self.checkNecessaryParams(dailyTypeCode, endStationID)

        if dailyTypeCode and endStationID and trainClass and schedule is not None:
            queryset = queryset.filter(runDay=dailyTypeCode, endStationID=endStationID,
                                       trainClass=trainClass, arrivalTime__startswith=schedule)
        elif dailyTypeCode and endStationID and trainClass is not None:
            queryset = queryset.filter(runDay=dailyTypeCode, endStationID=endStationID,
                                       trainClass=trainClass)
        elif dailyTypeCode and endStationID and schedule is not None:
            queryset = queryset.filter(runDay=dailyTypeCode, endStationID=endStationID,
                                       arrivalTime__startswith=schedule)
        elif dailyTypeCode and endStationID is not None:
            queryset = queryset.filter(runDay=dailyTypeCode, endStationID=endStationID)
        if queryset:
            return queryset
        else:
            raise ptuBusErrorExcpetion(detail={"error": "파라메터 값이 잘못되었습니다.", "code" : "-3" ,"parameter" :
                {"dailyTypeCode" : dailyTypeCode, "endStationID" : endStationID, "trainClass" : trainClass, "schedule" : schedule}},
                                       status_code=status.HTTP_400_BAD_REQUEST)

    def checkNecessaryParams(self, dailyTypeCode, endStationID):
        if not dailyTypeCode and not endStationID:
            raise ptuBusErrorExcpetion(detail={"error": "endStationID와 startStationID가 입력되지 않았습니다.", "code": "-2"},
                                   status_code=status.HTTP_400_BAD_REQUEST)
        elif not dailyTypeCode:
            raise ptuBusErrorExcpetion(detail={"error": "startStationID가 입력되지 않았습니다.", "code" : "-1"}, status_code=status.HTTP_400_BAD_REQUEST)
        elif not endStationID:
            raise ptuBusErrorExcpetion(detail={"error": "endStationID가 입력되지 않았습니다.", "code" : "-1"}, status_code=status.HTTP_400_BAD_REQUEST)
