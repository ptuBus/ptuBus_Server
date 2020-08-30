from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import SubwayParsing
from ptuBusServer.Serializers import SubwayTimeTableSerializer
from ptuBusServer.Models import SubwayTimeTableModel

class SubwayListView(APIView):
    def get(self, request):
        count = 1
        try:
            SubwayTimeTableModel.objects.all().delete()
        except ConnectionResetError:
            SubwayTimeTableModel.objects.all().delete()
        data = SubwayParsing().parsing()
        for dailyList in data:
            for table in dailyList:
                SubwayTimeTableModel(
                    id = count,
                    startStationName=table['startStationName'],
                    endStationName=table['endStationName'],
                    dailyTypeCode=table['dailyTypeCode'],
                    upDownTypeCode=table['upDownTypeCode'],
                    schedule = table['schedule'],
                    isExpress = int(table['isExpress']),
                    ).save()
                count += 1
        data = SubwayTimeTableModel.objects.all()
        serializer = SubwayTimeTableSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)