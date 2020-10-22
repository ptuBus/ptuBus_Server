from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusServer.Serializers import SubwayLineSerializer
from ptuBusServer.Models import SubwayLineModel

class SubwayLineListView(APIView):
    def get(self, request):
        data = SubwayLineModel.objects.all()
        serializer = SubwayLineSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)