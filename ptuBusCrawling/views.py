from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views import View
from .models import *
from ptuBusCrawling.serializers import SubwaySerializer, SchoolBusSerializer
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class SubwayListView(View):
    def get(self, request):
        count = 1
        subway = SubwayParsing()
        SubwayList.objects.all().delete()
        data = subway.parsing()
        for dailyList in data:
            for table in dailyList:
                SubwayList(
                    pk = count,
                    arrTime = table['arrTime'],
                    dailyTypeCode=table['dailyTypeCode'],
                    subwayStationNm=table['subwayStationNm'],
                    endSubwayStationNm=table['endSubwayStationNm'],
                    upDownTypeCode=table['upDownTypeCode'],
                    ExpressType=int(table['ExpressType']),
                    ).save()
                count += 1
        snippets = SubwayList.objects.all()
        serializer = SubwaySerializer(snippets, many=True)
        return JSONResponse(serializer.data, status=201)

class SchoolListView(View):
    def get(self, request):
        count = 1
        school = SchoolParsing()
        SchoolBusList.objects.all().delete()
        data = school.parsingData()
        for dailyList in data:
            for table in dailyList:
                SchoolBusList(
                    id = count,
                    arrTime = table['arrTime'],
                    startStationID = table['startStationID'],
                    startStationNm = table['startStationNm'],
                    endStationID = table['endStationID'],
                    endStationNm = table['endStationNm'],
                    upDownTypeCode = table['upDownTypeCode'],
                    ).save()
                count += 1
        snippets = SchoolBusList.objects.all()
        serializer = SchoolBusSerializer(snippets, many=True)
        return JSONResponse(serializer.data, status=201)
