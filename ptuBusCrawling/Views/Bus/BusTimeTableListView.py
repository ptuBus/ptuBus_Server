from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import BusTimeTableParsing
from ptuBusCrawling.Serializers import BusTimeTableSerializer
from ptuBusCrawling.Models import BusTimeTableModel

class BusTimeTableListView(APIView):
    def get(self, request):
        try:
            BusTimeTableModel.objects.all().delete()
        except ConnectionResetError:
            BusTimeTableModel.objects.all().delete()
        BusTimeTableParsing().parsing()
        data = BusTimeTableModel.objects.all()
        serializer = BusTimeTableSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)