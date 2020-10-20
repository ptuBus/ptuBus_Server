from django.db import models

class SubwayStationModel(models.Model):
    id = models.IntegerField(primary_key=True)
    stationName = models.CharField(max_length = 100)
    stationCode = models.CharField(max_length = 100)
    lineCode = models.CharField(max_length = 100)
    railLineCode = models.CharField(max_length = 100)

    class Meta:
        db_table = 'SubwayStationData'