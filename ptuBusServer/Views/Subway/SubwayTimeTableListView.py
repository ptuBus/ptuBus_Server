from ptuBusServer.Serializers import SubwayTimeTableSerializer
from ptuBusServer.Models import SubwayTimeTableModel
from rest_framework import generics
from rest_framework import status
from ..ptuBusErrorExcpetion import ptuBusErrorExcpetion

class SubwayTimeTableListView(generics.ListAPIView):
    serializer_class = SubwayTimeTableSerializer

    def get_queryset(self):
        queryset = SubwayTimeTableModel.objects.all()

        dailyTypeCode = self.request.query_params.get('dailyTypeCode', None)
        upDownTypeCode = self.request.query_params.get('upDownTypeCode', None)
        isExpress = self.request.query_params.get('isExpress', None)
        schedule = self.request.query_params.get('schedule', None)

        if dailyTypeCode and upDownTypeCode and isExpress and schedule is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, isExpress=isExpress, schedule__startswith=schedule)
        elif dailyTypeCode and upDownTypeCode and schedule is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, schedule__startswith=schedule)
        elif dailyTypeCode and upDownTypeCode and isExpress is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, isExpress=isExpress)
        elif dailyTypeCode and upDownTypeCode is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode)
        if queryset:
            return queryset
        else:
            raise ptuBusErrorExcpetion(detail={"error": "파라메터 값이 잘못되었습니다.", "code" : "-3" ,"parameter" :
                {"startStationID" : dailyTypeCode, "upDownTypeCode" : upDownTypeCode, "isExpress" : isExpress, "schedule" : schedule}},
                status_code=status.HTTP_400_BAD_REQUEST)
