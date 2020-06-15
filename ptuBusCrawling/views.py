from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views import View
import ssl
from ptuBusCrawling.Crawler.Subway.SubwayParsing import SubwayParsing
from ptuBusCrawling.models.Subway.SubwayTimeTableModel import SubwayTimeTableModel
from ptuBusCrawling.Serializer.Subway.SubwayTimeTableSerializer import SubwayTimeTableSerializer
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
        SubwayTimeTableModel.objects.all().delete()
        data = subway.parsing()
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
        return JSONResponse(serializer.data, status=201)
#
# class SchoolListView(View):
#     def get(self, request):
#         count = 1
#         school = SchoolParsing()
#         SchoolBusList.objects.all().delete()
#         data = school.parsingData()
#         for dailyList in data:
#             for table in dailyList:
#                 SchoolBusList(
#                     id = count,
#                     arrTime = table['arrTime'],
#                     startStationID = table['startStationID'],
#                     startStationNm = table['startStationNm'],
#                     endStationID = table['endStationID'],
#                     endStationNm = table['endStationNm'],
#                     upDownTypeCode = table['upDownTypeCode'],
#                     ).save()
#                 count += 1
#         snippets = SchoolBusList.objects.all()
#         serializer = SchoolBusSerializer(snippets, many=True)
#         return JSONResponse(serializer.data, status=201)
