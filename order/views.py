import ast
import datetime
import uuid
from django.db.models import F
from alipay import AliPay  # 阿里支付包
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views.generic.base import View

from cart.cartmanager import *
from cart.models import *
from order.models import *
from userapp.models import *
from userapp.views import checkLogin


class OrderView(View):
    @checkLogin(r'/order/')
    def get(self, request):
        user = request.session.get('user')
        cartitems = ast.literal_eval(request.GET.get('cartitems'))
        print(cartitems, 'type=', type(cartitems))
        if isinstance(cartitems, dict):
            cartitems = (cartitems,)
        for cart in cartitems:
            for key in cart.keys():
                cart[key] = int(cart[key])
        print('cartitems = ', cartitems)
        cartitemlist = [getCartManger(request).get_cartitems(**data) for data in cartitems if data]
        print(cartitemlist)
        # for item in cartitems:    # 将json字符串转化为字典对象
        #     item = {key: int(value) for key, value in item.items()}
        #
        #     print(item)
        # 获取用户默认收货地址
        # user.address_set.get(isdefault=True)
        address = Address.objects.get(userinfo=user, isdefault=True)
        # cm = CartItem.objects.filter(goodsid=int(cartitems['goodsid']), sizeid=int(cartitems['sizeid']), colorid=int(cartitems['colorid']))
        # print(cm)
        # print('address = ', address)
        # 获取支付的总金额
        totalPrice = 0
        for cartitem in cartitemlist:
            totalPrice += cartitem.getTotalPrice()
        return render(request, 'order.html', locals())

    def post(self, request):
        return HttpResponse('xxx')


class ToPayView(View):
    @checkLogin(r'/order/pay/')
    def get(self, request):
        # 1.插入Oder表中的数据
        # 获取请求参数
        data = {
            'out_trade_num': uuid.uuid4().hex,
            'order_num': datetime.datetime.today().strftime('%Y%m%d%H%M%S'),
            'payway': request.GET.get('payway'),
            'address': Address.objects.get(id=request.GET.get('address')),
            'user': request.session.get('user'),

        }
        orderobj = Order.objects.create(**data)

        # 2,插入数据到orderItem表中的数据
        cartitems = ast.literal_eval(request.GET.get('cartitems'))
        for cart in cartitems:
            for key in cart.keys():
                cart[key] = int(cart[key])
        print(cartitems)
        amount = float(request.GET.get('totalprice', 0))
        amount = '%.2f' % amount
        print('amount=', amount)

        orderItemList = [OrderItem.objects.create(order=orderobj, **item) for item in cartitems if item]

        # 3.获取扫描支付页面
        alipay = AliPay(
            appid='2021000116684129',  # 沙箱应用id
            app_notify_url='http://127.0.0.1:8000/order/checkPay/',  # 默认回调的url
            app_private_key_string=open('testapp/keys/my_private_key.txt').read(),  # 个人私钥
            alipay_public_key_string=open('testapp/keys/alipay_public_key.txt').read(),  # 支付宝公钥
            sign_type='RSA2',  # 加密方式
            debug=True,  # 默认为False；True代表沙箱模式

        )
        print('orderid=', orderobj.out_trade_num)
        order_string = alipay.api_alipay_trade_page_pay(
            subject='黒商人',
            out_trade_no=orderobj.out_trade_num,
            total_amount=str(amount),
            return_url='http://127.0.0.1:8000/order/checkPay/',
            notify_url='http://127.0.0.1:8000/order/checkPay/',  # 可选

        )

        # 获取扫码支付的请求地址
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        return redirect(pay_url)


# 校验是否支付完成
class checkPayView(View):
    def get(self, request):
        params = request.GET.dict()
        out_trade_num = params.get('out_trade_no')
        print('params = {}'.format(params))
        alipay = AliPay(
            appid='2021000116684129',  # 沙箱应用id
            app_notify_url='http://127.0.0.1:8000/order/checkPay/',  # 默认回调的url
            app_private_key_string=open('testapp/keys/my_private_key.txt').read(),  # 个人私钥
            alipay_public_key_string=open('testapp/keys/alipay_public_key.txt').read(),  # 支付宝公钥
            sign_type='RSA2',  # 加密方式
            debug=True,  # 默认为False；True代表沙箱模式

        )
        response = alipay.api_alipay_trade_query(out_trade_num)
        code = response.get('code')
        sign = params.pop('sign')
        # if alipay.verify(params, sign):
        if code == '10000' and response.get('trade_status') == "TRADE_SUCCESS":
            # 订单改为已支付状态
            order = Order.objects.get(out_trade_num=out_trade_num)
            order.status = '已支付'
            order.save()
            orderitemlist = order.orderitem_set.all()  # all() 将queryset转化为object对象
            # 将订单的商品从购物车表cart中删除
            [CartItem.objects.filter(goodsid=item.goodsid, colorid=item.colorid, sizeid=item.sizeid,
                                     user=request.session.get('user')).delete() for item in orderitemlist if item]
            print(orderitemlist)
            # 修改库存
            [Inventory.objects.filter(goods_id=item.goodsid, color_id=item.colorid, size_id=item.sizeid).update(count=F('count')-item.count) for item in
             orderitemlist if item]

            return redirect(reverse('cart:gocart'))
        return HttpResponse('paying failed！')
