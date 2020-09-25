import math

from django.db import models

# Create your models here.
from goods.models import *


class CartItem(models.Model):
    goodsid = models.PositiveIntegerField()
    colorid = models.PositiveIntegerField()
    sizeid = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    isdelete = models.BooleanField(default=False)
    user = models.ForeignKey('userapp.UserInfo', on_delete=models.CASCADE)

    def getColor(self):
        return Color.objects.get(pk=self.colorid)

    def getGoods(self):
        return Goods.objects.get(pk=self.goodsid)

    def getSize(self):
        return Size.objects.get(pk=self.sizeid)

    def getTotalPrice(self):
        return self.getGoods().price * int(self.count)

    class Meta:
        unique_together = ['goodsid', 'colorid', 'sizeid']

