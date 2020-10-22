from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusServer.Serializers import SubwayStationSerializer
from ptuBusServer.Models import SubwayStationModel

class SubwayStationListView(APIView):
    def get(self, request):
        data = SubwayStationModel.objects.all()
        serializer = SubwayStationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)