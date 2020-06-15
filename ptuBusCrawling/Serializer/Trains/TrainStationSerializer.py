from rest_framework import serializers
from ptuBusCrawling.models.Trains.TrainStationModel import TrainStationModel

class TrainStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainStationModel
        fields = ('id', 'startStationName', 'startStationID', 'endStationName', 'endStationID')
