from django.db import models

class BusTerminalModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationID = models.CharField(max_length=100)
    startStationName = models.CharField(max_length=100)
    endStationID = models.CharField(max_length=100)
    endStationName = models.CharField(max_length=100)
    isExpress = models.IntegerField()

    class Meta:
        db_table = 'BusTerminalModel'

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

class SchoolBusTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    arrTime = models.CharField(max_length=100)
    startStationID = models.CharField(max_length=100)
    startStationNm = models.CharField(max_length=100)
    endStationID = models.CharField(max_length=100)
    endStationNm = models.CharField(max_length=100)
    upDownTypeCode = models.CharField(max_length=20)

    class Meta:
        db_table = 'SchoolBusTimeTable'

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

class TrainStationModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length = 100)
    startStationID = models.CharField(max_length = 100)
    endStationName = models.CharField(max_length = 100)
    endStationID = models.CharField(max_length = 100)

    class Meta:
        db_table = 'TrainStation'

class TrainTimeTableModel(models.Model):
    id = models.IntegerField(primary_key=True)
    startStationName = models.CharField(max_length = 100)
    startStationID = models.CharField(max_length = 100)
    endStationName= models.CharField(max_length = 100)
    endStationID = models.CharField(max_length = 100)
    railName = models.CharField(max_length = 100)
    trainClass = models.CharField(max_length = 100)
    departureTime = models.CharField(max_length = 100)
    arrivalTime = models.CharField(max_length = 100)
    wasteTime = models.CharField(max_length = 100)
    runDay = models.CharField(max_length = 100)

    class Meta:
        db_table = 'TrainTimeTable'