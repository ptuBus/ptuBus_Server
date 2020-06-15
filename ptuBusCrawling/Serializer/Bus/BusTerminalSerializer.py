from rest_framework import serializers
from ptuBusCrawling.models.Bus.BusTerminalModel import BusTerminalModel

class BusTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTerminalModel
        fields = ('id', 'startStationID', 'startStationName', 'endStationID', 'endStationName', 'isExpress')
