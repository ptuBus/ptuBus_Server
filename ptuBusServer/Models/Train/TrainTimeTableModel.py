from django.db import models

class TrainTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length = 100)
    startStationID = models.CharField(max_length = 100)
    endStationName = models.CharField(max_length = 100)
    endStationID = models.CharField(max_length = 100)
    railName = models.CharField(max_length = 100)
    trainClass = models.CharField(max_length = 100)
    departureTime = models.CharField(max_length = 100)
    arrivalTime = models.CharField(max_length = 100)
    wasteTime = models.CharField(max_length = 100)
    runDay = models.CharField(max_length = 100)

    class Meta:
        db_table = 'TrainTimeTable'