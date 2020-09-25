# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 样板 》 WejoyArea
class Area(models.Model):
    areaid = models.IntegerField(primary_key=True)
    areaname = models.CharField(max_length=50)
    parentid = models.IntegerField()
    arealevel = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area'




class Address(models.Model):
    aname = models.CharField(max_length=30)
    aphone = models.CharField(max_length=11)
    addr = models.CharField(max_length=100)
    isdefault = models.BooleanField(default=False)
    userinfo = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'userapp_address'


class UserInfo(models.Model):
    uname = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'userapp_userinfo'


class Areas(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pid = models.ForeignKey('self', models.DO_NOTHING, db_column='pid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'
