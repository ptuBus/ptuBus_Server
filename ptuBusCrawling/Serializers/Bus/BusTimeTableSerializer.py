from rest_framework import serializers
from ptuBusCrawling.Models import BusTimeTableModel


class BusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTimeTableModel
        fields = (
            "id",
            "startStationName",
            "startStationID",
            "endStationName",
            "endStationID",
            "wasteTime",
            "normalFare",
            "specialFare",
            "nightFare",
            "schedule",
            "nightschedule",
            "isExpress",
        )
