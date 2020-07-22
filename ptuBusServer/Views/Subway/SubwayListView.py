from ptuBusServer.Serializers import SubwayTimeTableSerializer
from ptuBusServer.Models import SubwayTimeTableModel
from rest_framework import generics

class SubwayListView(generics.ListAPIView):
    serializer_class = SubwayTimeTableSerializer

    def get_queryset(self):
        queryset = SubwayTimeTableModel.objects.all()

        dailyTypeCode = self.request.query_params.get('dailyTypeCode', None)
        upDownTypeCode = self.request.query_params.get('upDownTypeCode', None)
        isExpress = self.request.query_params.get('isExpress', None)
        arrTime = self.request.query_params.get('arrTime', None)

        if dailyTypeCode and upDownTypeCode and isExpress and arrTime is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, isExpress=isExpress, arrTime__startswith=arrTime)
        elif dailyTypeCode and upDownTypeCode and arrTime is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, arrTime__startswith=arrTime)
        elif dailyTypeCode and upDownTypeCode and isExpress is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode, isExpress=isExpress)
        elif dailyTypeCode and upDownTypeCode is not None:
            queryset = queryset.filter(dailyTypeCode=dailyTypeCode, upDownTypeCode=upDownTypeCode)

        return queryset