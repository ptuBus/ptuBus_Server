from django.db import models

class SubwayTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    arrTime = models.CharField(max_length = 100)
    dailyTypeCode = models.CharField(max_length = 100)
    subwayStationNm = models.CharField(max_length = 100)
    endSubwayStationNm = models.CharField(max_length = 100)
    upDownTypeCode = models.CharField(max_length = 100)
    ExpressType = models.IntegerField()

    class Meta:
        db_table = 'SubwayTimeTable'