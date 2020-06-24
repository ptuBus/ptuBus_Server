from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import TrainStationParsing
from ptuBusCrawling.Serializers import TrainStationSerializer
from ptuBusCrawling.Models import TrainStationModel

class TrainStationListView(APIView):
    def get(self, request):
        count = 1
        TrainStationModel.objects.all().delete()
        data = TrainStationParsing().parsing()
        for table in data:
            TrainStationModel(
                id = count,
                startStationName = table['startStationName'],
                startStationID = table['startStationID'],
                endStationName=table['endStationName'],
                endStationID = table['endStationID'],
            ).save()
            count += 1
        snippets = TrainStationModel.objects.all()
        serializer = TrainStationSerializer(snippets, many=True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)