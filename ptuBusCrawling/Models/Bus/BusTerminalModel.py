from django.db import models

class BusTerminalModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationID = models.CharField(max_length=100)
    startStationName = models.CharField(max_length=100)
    endStationID = models.CharField(max_length=100)
    endStationName = models.CharField(max_length=100)
    isExpress = models.IntegerField()

    class Meta:
        db_table = 'BusTerminal'