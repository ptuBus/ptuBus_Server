from rest_framework import serializers
from ptuBusCrawling.models.SchoolBus.SchoolBusTimeTableModel import SchoolBusTimeTableModel

class SchoolBusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBusTimeTableModel
        fields = ('id', 'arrTime', 'startStationID', 'startStationNm', 'endStationID', 'endStationNm', 'upDownTypeCode')
