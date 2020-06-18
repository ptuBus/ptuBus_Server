from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import ssl
from ptuBusCrawling.Crawler import *
from .serializers import *
ssl._create_default_https_context = ssl._create_unverified_context

class SubwayListView(APIView):
    def get(self, request):
        count = 1
        SubwayTimeTableModel.objects.all().delete()
        data = SubwayParsing().parsing()
        for dailyList in data:
            for table in dailyList:
                SubwayTimeTableModel(
                    pk = count,
                    arrTime = table['arrTime'],
                    dailyTypeCode=table['dailyTypeCode'],
                    subwayStationNm=table['subwayStationNm'],
                    endSubwayStationNm=table['endSubwayStationNm'],
                    upDownTypeCode=table['upDownTypeCode'],
                    ExpressType=int(table['ExpressType']),
                    ).save()
                count += 1
        snippets = SubwayTimeTableModel.objects.all()
        print (snippets)
        serializer = SubwayTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SchooBuslListView(APIView):
    def get(self, request):
        count = 1
        school = SchoolParsing()
        SchoolBusTimeTableModel.objects.all().delete()
        data = school.parsingData()
        for dailyList in data:
            for table in dailyList:
                SchoolBusTimeTableModel(
                    id = count,
                    arrTime = table['arrTime'],
                    startStationID = table['startStationID'],
                    startStationNm = table['startStationNm'],
                    endStationID = table['endStationID'],
                    endStationNm = table['endStationNm'],
                    upDownTypeCode = table['upDownTypeCode'],
                    ).save()
                count += 1
        snippets = SchoolBusTimeTableModel.objects.all()
        serializer = SchoolBusTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BusTerminalListView(APIView):
    def get(self, request):
        count = 1
        BusTerminalModel.objects.all().delete()
        data = BusTerminalParsing().parsing()
        for table in data:
            BusTerminalModel(
                id = count,
                startStationID = table['startStationID'],
                startStationName = table['startStationName'],
                endStationID = table['endStationID'],
                endStationName = table['endStationName'],
                isExpress = int(table['isExpress']),
                ).save()
            count += 1
        snippets = BusTerminalModel.objects.all()
        serializer = BusTerminalSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BusTimeTableListView(APIView):
    def get(self, request):
        count = 1
        Bus = BusTerminalParsing()
        BusTimeTableModel.objects.all().delete()
        data = BusTimeTableParsing(Bus.parsing()).parsing()
        for table in data:
            BusTimeTableModel(
                id = count,
                startStationID = table['startStationID'],
                startStationName = table['startStationName'],
                endStationID = table['endStationID'],
                endStationName = table['endStationName'],
                wasteTime = table['wasteTime'],
                normalFare = table['normalFare'],
                specialFare = table['specialFare'],
                nightFare = table['nightFare'],
                schedule = table['schedule'],
                nightschedule = table['nightschedule'],
                ).save()
            count += 1
        snippets = BusTimeTableModel.objects.all()
        serializer = BusTimeTableSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)