from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusServer.Serializers import TrainStationSerializer
from ptuBusServer.Models import TrainStationModel


class TrainStationListView(APIView):
    def get(self, request):
        data = TrainStationModel.objects.all()
        serializer = TrainStationSerializer(data, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
