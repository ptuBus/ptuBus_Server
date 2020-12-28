from rest_framework import serializers
from ptuBusServer.Models import BusTerminalModel


class BusTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTerminalModel
        fields = (
            "id",
            "startStationName",
            "startStationID",
            "endStationName",
            "endStationID",
            "isExpress",
        )
