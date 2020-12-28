from django.db import models


class SchoolBusTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length=100)
    startStationID = models.CharField(max_length=100)
    endStationName = models.CharField(max_length=100)
    endStationID = models.CharField(max_length=100)
    arrTime = models.CharField(max_length=100)
    upDownTypeCode = models.CharField(max_length=20)

    class Meta:
        db_table = "SchoolBusTimeTable"
