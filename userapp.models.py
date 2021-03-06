# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.IntegerField(primary_key=True)
    areaname = models.CharField(max_length=50)
    parentid = models.IntegerField()
    arealevel = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area'


class Areas(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pid = models.ForeignKey('self', models.DO_NOTHING, db_column='Pid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GoodsCategory(models.Model):
    cname = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsColor(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'goods_color'


class GoodsGoods(models.Model):
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(GoodsCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_goods'


class GoodsGoodsdetail(models.Model):
    gdurl = models.CharField(max_length=100)
    gdname = models.ForeignKey('GoodsGoodsdetailname', models.DO_NOTHING)
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_goodsdetail'


class GoodsGoodsdetailname(models.Model):
    gdname = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'goods_goodsdetailname'


class GoodsInventory(models.Model):
    count = models.IntegerField()
    color = models.ForeignKey(GoodsColor, models.DO_NOTHING)
    goods = models.ForeignKey(GoodsGoods, models.DO_NOTHING)
    size = models.ForeignKey('GoodsSize', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goods_inventory'


class GoodsSize(models.Model):
    sname = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'goods_size'


class UserappAddress(models.Model):
    aname = models.CharField(max_length=30)
    aphone = models.CharField(max_length=11)
    addr = models.CharField(max_length=100)
    isdefault = models.IntegerField()
    userinfo = models.ForeignKey('UserappUserinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userapp_address'


class UserappUserinfo(models.Model):
    uname = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'userapp_userinfo'


class WejoyArea(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    parent_id = models.PositiveSmallIntegerField()
    cname = models.CharField(max_length=120)
    ctype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wejoy_area'
