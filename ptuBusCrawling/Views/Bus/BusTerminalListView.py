from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import BusTerminalParsing
from ptuBusCrawling.Serializers import BusTerminalSerializer
from ptuBusCrawling.Models import BusTerminalModel

class BusTerminalListView(APIView):
    def get(self, request):
        count = 1
        BusTerminalModel.objects.all().delete()
        data = BusTerminalParsing().parsing()
        for table in data:
            BusTerminalModel(
                id = count,
                startStationID = table['startStationID'],
                startStationName = table['startStationName'],
                endStationID = table['endStationID'],
                endStationName = table['endStationName'],
                isExpress = int(table['isExpress']),
                ).save()
            count += 1
        snippets = BusTerminalModel.objects.all()
        serializer = BusTerminalSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)