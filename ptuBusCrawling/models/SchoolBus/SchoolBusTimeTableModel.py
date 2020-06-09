from django.db import models

class SchoolBusTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    arrTime = models.CharField(max_length = 100)
    startStationID = models.IntegerField()
    startStationNm = models.CharField(max_length = 100)
    endStationID = models.IntegerField()
    endStationNm = models.CharField(max_length = 100)
    upDownTypeCode = models.CharField(max_length = 20)

    class Meta:
        db_table = 'SchoolBusTimeTable'