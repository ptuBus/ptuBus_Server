from django.db import models

class BusTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationID = models.CharField(max_length = 100)
    startStationName = models.CharField(max_length = 100)
    endStationID = models.CharField(max_length = 100)
    endStationName = models.CharField(max_length = 100)
    wasteTime = models.CharField(max_length = 100)
    normalFare = models.CharField(max_length = 100)
    specialFare = models.CharField(max_length = 100)
    nightFare = models.CharField(max_length = 100)
    schedule = models.CharField(max_length = 100)
    nightschedule = models.CharField(max_length = 100)

    class Meta:
        db_table = 'BusTimeTableModel'