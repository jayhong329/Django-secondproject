from django.db import models
from datetime import datetime

# Create your models here.

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=20, unique=True)
    member_password = models.CharField(max_length=128)
    member_bitrh = models.DateField()
    member_address = models.CharField(max_length=200, null=True)
    last_update = models.DateTimeField(default=datetime.now())

class Member_log(models.Model):
    member_id = models.IntegerField(primary_key=True)
    member_login = models.IntegerField(unique=True)
    provider = models.CharField(max_length=50)
    provider_id_google = models.CharField(max_length=50)
    provider_id_line = models.CharField(max_length=50)
    provider_id_fb = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50)

class Meta:
    ds_table = 'member'  # 指定的資料表名稱