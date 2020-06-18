from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import SchoolParsing
from ptuBusCrawling.Serializers import SchoolBusTimeTableSerializer
from ptuBusCrawling.Models import SchoolBusTimeTableModel

class SchooBuslListView(APIView):
    def get(self, request):
        count = 1
        school = SchoolParsing()
        SchoolBusTimeTableModel.objects.all().delete()
        data = school.parsingData()
        for dailyList in data:
            for table in dailyList:
                SchoolBusTimeTableModel(
                    id = count,
                    arrTime = table['arrTime'],
                    startStationID = table['startStationID'],
                    startStationNm = table['startStationNm'],
                    endStationID = table['endStationID'],
                    endStationNm = table['endStationNm'],
                    upDownTypeCode = table['upDownTypeCode'],
                    ).save()
                count += 1
        snippets = SchoolBusTimeTableModel.objects.all()
        serializer = SchoolBusTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)