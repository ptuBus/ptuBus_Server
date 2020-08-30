from ptuBusServer.Serializers import SchoolBusTimeTableSerializer
from ptuBusServer.Models import SchoolBusTimeTableModel
from rest_framework import generics
from rest_framework import status
from ..ptuBusErrorExcpetion import ptuBusErrorExcpetion

class SchoolBusTimeTableListView(generics.ListAPIView):
    serializer_class = SchoolBusTimeTableSerializer

    def get_queryset(self):
        queryset = SchoolBusTimeTableModel.objects.all()

        startStationID = self.request.query_params.get('startStationID', None)
        endStationID = self.request.query_params.get('endStationID', None)
        upDownTypeCode = self.request.query_params.get('upDownTypeCode', None)
        schedule = self.request.query_params.get('schedule', None)
        self.checkNecessaryParams(startStationID, endStationID, upDownTypeCode)

        if startStationID and endStationID and upDownTypeCode and schedule is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID=endStationID,
                                       upDownTypeCode=upDownTypeCode, schedule__startswith=schedule)
        elif startStationID and endStationID and upDownTypeCode is not None:
            queryset = queryset.filter(startStationID=startStationID, endStationID=endStationID,
                                       upDownTypeCode=upDownTypeCode)
        if queryset:
           return queryset
        else:
            raise ptuBusErrorExcpetion(detail={"error": "파라메터 값이 잘못되었습니다.", "code": "-3", "parameter":
                    {"startStationID": startStationID, "endStationID": endStationID, "upDownTypeCode" : upDownTypeCode, "schedule" : schedule}},
                                           status_code=status.HTTP_400_BAD_REQUEST)

    def checkNecessaryParams(self, startStationID, endStationID, upDownTypeCode):
        if not endStationID and not startStationID and not upDownTypeCode:
            raise ptuBusErrorExcpetion(detail={"error": "endStationID, startStationID, upDownTypeCode가 입력되지 않았습니다.", "code": "-2"},
                                   status_code=status.HTTP_400_BAD_REQUEST)
        elif not startStationID:
            raise ptuBusErrorExcpetion(detail={"error": "startStationID가 입력되지 않았습니다.", "code" : "-1"}, status_code=status.HTTP_400_BAD_REQUEST)
        elif not endStationID:
            raise ptuBusErrorExcpetion(detail={"error": "endStationID가 입력되지 않았습니다.", "code" : "-1"}, status_code=status.HTTP_400_BAD_REQUEST)
        elif not upDownTypeCode:
            raise ptuBusErrorExcpetion(detail={"error": "upDownTypeCode가 입력되지 않았습니다.", "code" : "-1"}, status_code=status.HTTP_400_BAD_REQUEST)