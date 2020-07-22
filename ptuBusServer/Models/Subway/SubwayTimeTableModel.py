from django.db import models

class SubwayTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length = 100)
    endStationName = models.CharField(max_length = 100)
    dailyTypeCode = models.CharField(max_length = 100)
    upDownTypeCode = models.CharField(max_length = 100)
    arrTime = models.CharField(max_length = 100)
    isExpress = models.IntegerField()

    class Meta:
        db_table = 'SubwayTimeTable'