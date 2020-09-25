from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
# Create your views here.
from django.views.generic.base import View
from cart.cartmanager import *
from cart.models import CartItem
from userapp.views import checkLogin


class AddCartView(View):
    def post(self, request):
        data = request.POST.dict()
        print(data)
        # 获取当前操作类型
        flag = request.POST.get('flag')
        # 创建cartManager对象
        cartManagerObj = getCartManger(request)
        if flag == 'add':
            # 加入购物车操作
            cartManagerObj.add(**data)
        elif flag == 'plus':
            # 修改商品的数量（add）
            cartManagerObj.update(step=1, **data)
        elif flag == 'reduce':
            # 修改商品的数量（delete）
            cartManagerObj.update(step=-1, **data)
        elif flag == 'delete':
            # 移除该商品
            cartManagerObj.delete(**data)
        return redirect(reverse('cart:gocart'))


class GoCartView(View):
    @checkLogin(r'/cart/gocart/')
    def get(self, request):
        # 创建CartManager对象
        cartMangerObj = getCartManger(request)
        # 查询所有所有购物信息
        cartList =cartMangerObj.queryAll()
        print(cartList)
        return render(request, 'cart.html', locals())