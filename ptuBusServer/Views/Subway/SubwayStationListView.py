from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusServer.Serializers import BusTerminalSerializer
from ptuBusServer.Models import BusTerminalModel
import json

class SubwayStationListView(APIView):
    def get(self, request):
        with open('data.json') as json_file:
            json_data = json.load(json_file)
        return JsonResponse(json_data)

