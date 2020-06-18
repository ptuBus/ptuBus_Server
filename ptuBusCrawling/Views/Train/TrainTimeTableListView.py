from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import TrainStationParsing, TrainTimeTableParsing
from ptuBusCrawling.Serializers import TrainTimeTableSerializer
from ptuBusCrawling.Models import TrainTimeTableModel

class TrainTimeTableListView(APIView):
    def get(self, request):
        count = 1
        Train = TrainStationParsing()
        TrainTimeTableModel.objects.all().delete()
        data = TrainTimeTableParsing(Train.parsing()).parsing()
        for table in data:
            TrainTimeTableModel(
                id = count,
                startStationName = table['startStationName'],
                startStationID = table['startStationID'],
                endStationName = table['endStationName'],
                endStationID = table['endStationID'],
                railName = table['railName'],
                trainClass = table['trainClass'],
                departureTime = table['departureTime'],
                arrivalTime = table['arrivalTime'],
                wasteTime = table['wasteTime'],
                runDay = table['runDay'],
            ).save()
            count += 1
        snippets = TrainTimeTableModel .objects.all()
        serializer = TrainTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
