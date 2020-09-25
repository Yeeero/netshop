from django.db import models


# Create your models here.
from goods.models import *
from userapp.models import *


class Order(models.Model):
    out_trade_num = models.UUIDField()  # 该字段只有唯一值，用于交易时的交易凭证
    order_num = models.CharField(max_length=50)
    trade_no = models.CharField(max_length=120)
    status = models.CharField(max_length=20, default='待支付')
    payway = models.CharField(max_length=20, default='alipay')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class OrderItem(models.Model):
    goodsid = models.PositiveIntegerField()
    colorid = models.PositiveIntegerField()
    sizeid = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def getGoods(self):
        return Goods.objects.get(pk=self.goodsid)

    def getColor(self):
        return Color.objects.get(pk=self.colorid)

    def getSize(self):
        return Size.objects.get(pk=self.sizeid)
