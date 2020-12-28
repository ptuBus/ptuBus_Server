from django.db import models


class SubwayLineModel(models.Model):
    id = models.IntegerField(primary_key=True)
    lineName = models.CharField(max_length=100)
    lineCode = models.CharField(max_length=100)
    lineColorCode = models.CharField(max_length=100)
    lineSaidName = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "SubwayLineData"
