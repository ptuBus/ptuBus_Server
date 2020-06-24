from rest_framework import serializers
from ptuBusCrawling.Models import SubwayTimeTableModel

class SubwayTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayTimeTableModel
        fields = ('id', 'startStationName', 'endStationName', 'dailyTypeCode', 'upDownTypeCode', 'arrTime', 'isExpress')