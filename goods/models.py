# Create your models here.
import collections

from django.db import models


class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __str__(self):
        return 'Category:%s' % self.cname


class Goods(models.Model):
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')

    def __str__(self):
        return 'Goods:%s' % self.gname

    def getGImg(self):
        return self.inventory_set.first().color.colorurl  # 获取该商品库存的第一个对象

    # 获取商品所有颜色对象
    def getColor(self):
        colorlist = []
        for inventory in self.inventory_set.all():
            color = inventory.color
            if color not in colorlist:
                colorlist.append(color)
        return colorlist

    def getSize(self):
        sizelist = []
        for inventory in self.inventory_set.all():
            size = inventory.size
            if size not in sizelist:
                sizelist.append(size)
        return sizelist

    def getGoodsDetial(self):
        gdlist = collections.OrderedDict()     # 创建一个有序字典（key为详情名称；value为图片列表）
        for goodsdetal in self.goodsdetail_set.all():
            gdname = goodsdetal.goodsDetailName.gdname
            if not gdlist.get(gdname):
                gdlist[gdname] = [goodsdetal.gdurl]
            else:
                gdlist[gdname].append(goodsdetal.gdurl)
        return gdlist


class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')


class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __str__(self):
        return 'Size:%s' % self.sname


class Inventory(models.Model):
    count = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __str__(self):
        return 'GoodsDetailName:%s' % self.gdname


class GoodsDetail(models.Model):
    gdurl = models.ImageField(upload_to='')
    goodsDetailName = models.ForeignKey(GoodsDetailName, on_delete=models.CASCADE, db_column='gdname_id')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
