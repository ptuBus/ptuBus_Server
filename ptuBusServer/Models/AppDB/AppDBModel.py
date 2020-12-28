from django.db import models


class AppDBModel(models.Model):
    id = models.AutoField(primary_key=True)
    fileKey = models.CharField(max_length=100)

    class Meta:
        db_table = "AppDBModel"
