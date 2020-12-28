from rest_framework import serializers
from ptuBusServer.Models import SubwayStationModel


class SubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStationModel
        fields = (
            "id",
            "stationName",
            "stationCode",
            "lineCode",
            "railLineCode",
        )
