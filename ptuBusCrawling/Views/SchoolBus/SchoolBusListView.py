from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import SchoolParsing
from ptuBusCrawling.Serializers import SchoolBusTimeTableSerializer
from ptuBusCrawling.Models import SchoolBusTimeTableModel

class SchoolBusListView(APIView):
    def get(self, request):
        count = 1
        school = SchoolParsing()
        SchoolBusTimeTableModel.objects.all().delete()
        data = school.parsingData()
        for dailyList in data:
            for table in dailyList:
                SchoolBusTimeTableModel(
                    id = count,
                    startStationName=table['startStationName'],
                    startStationID = table['startStationID'],
                    endStationName=table['endStationName'],
                    endStationID = table['endStationID'],
                    arrTime=table['arrTime'],
                    upDownTypeCode = table['upDownTypeCode'],
                ).save()
                count += 1
        data = SchoolBusTimeTableModel.objects.all()
        serializer = SchoolBusTimeTableSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)