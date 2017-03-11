from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class myuesr(models.Model):
    id=models.AutoField
    user_name=models.CharField(max_length=30)
    user_pass=models.CharField(max_length=50)
    user_regdate=models.DateTimeField(default=timezone.now)
    user_status=models.IntegerField(default=1)
    class Meta:
        db_table='myuser'
