from django.forms import widgets
from rest_framework import serializers
from ptuBusCrawling.models import SubwayList, SchoolBusList

class SubwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayList
        fields = ('id', 'arrTime', 'dailyTypeCode', 'subwayStationNm', 'endSubwayStationNm', 'upDownTypeCode', 'ExpressType')

class SchoolBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBusList
        fields = ('id', 'arrTime', 'startStationID', 'startStationNm', 'endStationID', 'endStationNm', 'upDownTypeCode')