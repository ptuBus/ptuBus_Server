from rest_framework import serializers
from ptuBusServer.Models import AppDBModel


class AppDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDBModel
        fields = ("id", "fileKey")
