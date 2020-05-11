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
                    pk = count,
                    arrTime = table['arrTime'],
                    dailyTypeCode=table['dailyTypeCode'],
                    subwayStationNm=table['subwayStationNm'],
                    endSubwayStationNm=table['endSubwayStationNm'],
                    upDownTypeCode=table['upDownTypeCode'],
                    ExpressType=int(table['ExpressType']),
                    ).save()
                count += 1
        snippets = SubwayTimeTableModel.objects.all()
        serializer = SubwayTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)