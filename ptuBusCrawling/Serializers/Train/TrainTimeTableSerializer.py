from rest_framework import serializers
from ptuBusCrawling.Models import TrainTimeTableModel


class TrainTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainTimeTableModel
        fields = (
            "id",
            "startStationName",
            "startStationID",
            "endStationName",
            "endStationID",
            "railName",
            "trainClass",
            "departureTime",
            "arrivalTime",
            "wasteTime",
            "runDay",
        )
