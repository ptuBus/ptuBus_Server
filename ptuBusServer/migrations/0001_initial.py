# Generated by Django 3.0.5 on 2020-08-30 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusTerminalModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('startStationID', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('endStationID', models.CharField(max_length=100)),
                ('isExpress', models.IntegerField()),
            ],
            options={
                'db_table': 'BusTerminal',
            },
        ),
        migrations.CreateModel(
            name='BusTimeTableModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('startStationID', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('endStationID', models.CharField(max_length=100)),
                ('wasteTime', models.CharField(max_length=100)),
                ('normalFare', models.CharField(max_length=100)),
                ('specialFare', models.CharField(max_length=100)),
                ('nightFare', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=100)),
                ('nightschedule', models.CharField(max_length=100)),
                ('isExpress', models.IntegerField()),
            ],
            options={
                'db_table': 'BusTimeTable',
            },
        ),
        migrations.CreateModel(
            name='SchoolBusTimeTableModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('startStationID', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('endStationID', models.CharField(max_length=100)),
                ('arrTime', models.CharField(max_length=100)),
                ('upDownTypeCode', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'SchoolBusTimeTable',
            },
        ),
        migrations.CreateModel(
            name='SubwayTimeTableModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('dailyTypeCode', models.CharField(max_length=100)),
                ('upDownTypeCode', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=100)),
                ('isExpress', models.IntegerField()),
            ],
            options={
                'db_table': 'SubwayTimeTable',
            },
        ),
        migrations.CreateModel(
            name='TrainStationModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('startStationID', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('endStationID', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TrainStation',
            },
        ),
        migrations.CreateModel(
            name='TrainTimeTableModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startStationName', models.CharField(max_length=100)),
                ('startStationID', models.CharField(max_length=100)),
                ('endStationName', models.CharField(max_length=100)),
                ('endStationID', models.CharField(max_length=100)),
                ('railName', models.CharField(max_length=100)),
                ('trainClass', models.CharField(max_length=100)),
                ('departureTime', models.CharField(max_length=100)),
                ('arrivalTime', models.CharField(max_length=100)),
                ('wasteTime', models.CharField(max_length=100)),
                ('runDay', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TrainTimeTable',
            },
        ),
    ]