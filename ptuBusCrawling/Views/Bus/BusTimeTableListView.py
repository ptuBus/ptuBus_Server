from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import BusTimeTableParsing, BusTerminalParsing
from ptuBusCrawling.Serializers import BusTimeTableSerializer
from ptuBusCrawling.Models import BusTimeTableModel

class BusTimeTableListView(APIView):
    def get(self, request):
        count = 1
        BusTimeTableModel.objects.all().delete()
        Bus = BusTerminalParsing()
        data = BusTimeTableParsing(Bus.parsing()).parsing()
        for table in data:
            BusTimeTableModel(
                id = count,
                startStationID = table['startStationID'],
                startStationName = table['startStationName'],
                endStationID = table['endStationID'],
                endStationName = table['endStationName'],
                wasteTime = table['wasteTime'],
                normalFare = table['normalFare'],
                specialFare = table['specialFare'],
                nightFare = table['nightFare'],
                schedule = table['schedule'],
                nightschedule = table['nightschedule'],
                ).save()
            count += 1
        snippets = BusTimeTableModel.objects.all()
        serializer = BusTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)