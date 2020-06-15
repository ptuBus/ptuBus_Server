from rest_framework import serializers
from ptuBusCrawling.models.Subway import SubwayTimeTableModel

class SubwayTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayTimeTableModel
        fields = ('id', 'arrTime', 'dailyTypeCode', 'subwayStationNm', 'endSubwayStationNm', 'upDownTypeCode', 'ExpressType')
