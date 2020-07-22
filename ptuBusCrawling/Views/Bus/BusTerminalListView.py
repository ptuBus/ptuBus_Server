from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import BusTerminalParsing
from ptuBusServer.Serializers import BusTerminalSerializer
from ptuBusServer.Models import BusTerminalModel

class BusTerminalListView(APIView):
    def get(self, request):
        try:
            BusTerminalModel.objects.all().delete()
        except ConnectionResetError:
            BusTerminalModel.objects.all().delete()
        BusTerminalParsing().parsing()
        data = BusTerminalModel.objects.all()
        serializer = BusTerminalSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)