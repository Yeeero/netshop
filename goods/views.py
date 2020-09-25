import math

from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from django.views.generic.base import View

from goods.models import *


class IndexView(View):
    def get(self, request, cid=2, pagenum=1):
        categories = Category.objects.all()
        goodslist = Goods.objects.filter(category_id=cid).order_by('-id')

        # 分页
        paginator = Paginator(goodslist, 8)
        page = paginator.page(pagenum)
        # 每页开始
        begin = (pagenum - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1
        # 每页结束页
        end = begin + 9
        if end > paginator.num_pages:
            end = paginator.num_pages
        if end <= 10:
            begin = 1
        else:
            begin = end - 9
        pagelist = range(begin, end + 1)
        return render(request, 'index.html', locals())


# 装饰器: 获取历史浏览商品信息
def recommend_view(func):
    def wrapper(DetailView, request, goodsid, *args, **kwargs):
        goodsid = str(goodsid)
        # 获取存放在cookie中的goodsid
        cookie_str = request.COOKIES.get('recommend', '')
        # goods_id_list save all of goodsid
        goods_id_list = cookie_str.split()
        # 最终获取推荐的商品
        goodsObjectList = [Goods.objects.get(id=gsid) for gsid in goods_id_list if
                           gsid != goodsid and Goods.objects.get(id=gsid).category_id == Goods.objects.get(
                               pk=goodsid).category_id][:4]
        # 将goodsObjectList传递给get方法
        response = func(DetailView, request, goodsid, goodsObjectList, *args, **kwargs)
        # 判断goodsid是否存在于列表中，设置最新的goodsid
        if goodsid in goods_id_list:
            goods_id_list.remove(goodsid)
        goods_id_list.insert(0, goodsid)
        # 将goods_id_list中的数据存放到Cookie
        response.set_cookie('recommend', ' '.join(goods_id_list), max_age=3 * 24 * 60 * 60)
        return response

    return wrapper


class DetailView(View):
    @recommend_view
    def get(self, request, goodsid, recommendlist=[]):
        goods = Goods.objects.get(pk=goodsid)
        return render(request, 'goodsdetails.html', locals())
