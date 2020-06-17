from rest_framework import serializers
from ptuBusCrawling.models import *

class BusTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTerminalModel
        fields = ('id', 'startStationID', 'startStationName', 'endStationID', 'endStationName', 'isExpress')

class BusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTimeTableModel
        fields = ('id', 'startStationID', 'startStationName', 'endStationID', 'endStationName', 'wasteTime', 'normalFare',
                  'specialFare', 'nightFare', 'schedule', 'nightschedule')

class SchoolBusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBusTimeTableModel
        fields = ('id', 'arrTime', 'startStationID', 'startStationNm', 'endStationID', 'endStationNm', 'upDownTypeCode')

class SubwayTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayTimeTableModel
        fields = ('id', 'arrTime', 'dailyTypeCode', 'subwayStationNm', 'endSubwayStationNm', 'upDownTypeCode', 'ExpressType')

class TrainStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainStationModel
        fields = ('id', 'startStationName', 'startStationID', 'endStationName', 'endStationID')

class TrainTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainTimeTableModel
        fields = ('id', 'startStationName', 'startStationID', 'endStationName', 'endStationID', 'railName', 'trainClass',
                  'departureTime', 'arrivalTime', 'wasteTime', 'runDay')

