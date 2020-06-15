from rest_framework import serializers
from ptuBusCrawling.models.Bus.BusTimeTableModel import BusTimeTableModel

class BusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTimeTableModel
        fields = ('id', 'startStationID', 'startStationName', 'endStationID', 'endStationName', 'wasteTime', 'normalFare',
                  'specialFare', 'nightFare', 'schedule', 'nightschedule')
