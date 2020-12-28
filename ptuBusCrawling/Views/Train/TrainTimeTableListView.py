from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import TrainTimeTableParsing
from ptuBusServer.Serializers import TrainTimeTableSerializer
from ptuBusServer.Models import TrainTimeTableModel


class TrainTimeTableListView(APIView):
    def get(self, request):
        try:
            TrainTimeTableModel.objects.all().delete()
        except ConnectionResetError:
            TrainTimeTableModel.objects.all().delete()
        TrainTimeTableParsing().parsing()
        data = TrainTimeTableModel.objects.all()
        serializer = TrainTimeTableSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
