from rest_framework import serializers
from ptuBusServer.Models import SubwayLineModel


class SubwayLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayLineModel
        fields = (
            "id",
            "lineName",
            "lineCode",
            "lineColorCode",
            "lineSaidName",
        )
