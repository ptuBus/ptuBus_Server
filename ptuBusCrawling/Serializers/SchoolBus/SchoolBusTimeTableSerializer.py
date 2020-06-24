from rest_framework import serializers
from ptuBusCrawling.Models import SchoolBusTimeTableModel

class SchoolBusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBusTimeTableModel
        fields = ('id', 'startStationName', 'startStationID', 'endStationName', 'endStationID', 'arrTime', 'upDownTypeCode')