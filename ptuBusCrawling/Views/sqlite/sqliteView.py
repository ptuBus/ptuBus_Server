from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ptuBusCrawling.Crawler import makeSqlite


class sqliteView(APIView):
    def get(self, request):
        makeDataBase = makeSqlite()
        makeDataBase.diffDataBase()
        return Response(status=status.HTTP_201_CREATED)
