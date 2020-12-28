from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusServer.Serializers import AppDBSerializer
from ptuBusServer.Models import AppDBModel


class AppDBView(APIView):
    def get(self, request):
        data = AppDBModel.objects.all().order_by("-id")
        serializer = AppDBSerializer(data, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
