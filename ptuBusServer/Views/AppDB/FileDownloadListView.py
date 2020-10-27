from wsgiref.util import FileWrapper

from rest_framework import generics
from django.http import HttpResponse

class FileDownloadListView(generics.ListAPIView):
    def get(self, request):
        file = open("app.db", 'rb')
        response = HttpResponse(FileWrapper(file), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=app.db'
        return response