from django.db import models

class TrainStationModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length = 100)
    startStationID = models.CharField(max_length = 100)
    endStationName= models.CharField(max_length = 100)
    endStationID = models.CharField(max_length = 100)

    class Meta:
        db_table = 'TrainStation'