from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import SubwayParsing
from ptuBusCrawling.Serializers import SubwayTimeTableSerializer
from ptuBusCrawling.Models import SubwayTimeTableModel

class SubwayListView(APIView):
    def get(self, request):
        count = 1
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
                    arrTime = table['arrTime'],
                    isExpress = int(table['isExpress']),
                    ).save()
                count += 1
        snippets = SubwayTimeTableModel.objects.all()
        serializer = SubwayTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)