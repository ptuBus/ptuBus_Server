from rest_framework import serializers
from ptuBusCrawling.Models import BusTerminalModel


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
