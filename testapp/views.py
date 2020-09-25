from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from alipay import AliPay, ISVAliPay
# Create your views here.
from django.views.generic.base import View

# from utils.alipay import AliPay


class PayView(View):
    def get(self, request):
        return render(request, 'stu.html')

    def post(self, request):
        # 获取支付二维码界面
        import uuid
        # 获取请求参数
        amount = float(request.POST.get('amount', 0))
        amount = '%.2f' % amount
        print(uuid.uuid4().hex)
        # 业务处理 使用python sdk调用支付宝的支付接口
        # 支付宝信息  不能放在settings里 会报错
        app_private_key_string = open('testapp/keys/my_private_key.txt').read()
        alipay_public_key_string = open('testapp/keys/alipay_public_key.txt').read()
        print(alipay_public_key_string)
        alipay = AliPay(
            appid='2021000116684129',   # 沙箱应用id
            app_notify_url='http://127.0.0.1:8000/test/checkPay/',   # 默认回调的url
            app_private_key_string=app_private_key_string,   # 个人私钥
            alipay_public_key_string=alipay_public_key_string,  # 支付宝公钥
            sign_type='RSA2',   # 加密方式
            debug=True,     # 默认为False；True代表沙箱模式

        )

        # 获取扫码支付请求参数
        # 调用支付接口
        # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string 实际地址
        # 沙箱地址 https://openapi.alipaydev.com/gateway.do? + order_string 沙箱地址在alipay后面加上dev
        order_string = alipay.api_alipay_trade_page_pay(
            subject='黒商人',
            out_trade_no=uuid.uuid4().hex,
            total_amount=str(amount),
            return_url='http://127.0.0.1:8000/test/checkPay/',
            notify_url='http://127.0.0.1:8000/test/checkPay/',  # 可选

        )

        # 获取扫码支付的请求地址
        pay_url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        return redirect(pay_url)
        # return HttpResponseRedirect(url)
        # return JsonResponse({'alipay_url': pay_url})


# alipay = AliPay(appid='2016091100486702', app_notify_url='http://127.0.0.1:8000/test/checkPay/', app_private_key_path='testapp/keys/my_private_key.txt',
#                  alipay_public_key_path='testapp/keys/alipay_public_key.txt', return_url='http://127.0.0.1:8000/test/checkPay/', debug=True)


# 校验是否支付完成
def checkPay_view(request):
    # 获取所有请求参数
    params = request.GET.dict()
    # print(params)
    # # 移除并获取sign参数的值
    # sign = params.pop('sign')
    # print('sing =', sign)
    # # 校验是否支付成功
    # if AliPay.verify(request, data=params, signature=sign):
    #     return HttpResponse('支付成功！')
    # return HttpResponse('支付失败！')

    import uuid
    # 获取请求参数
    amount = float(request.POST.get('amount', 0))
    amount = '%.2f' % amount
    print(uuid.uuid4().hex)
    # 业务处理 使用python sdk调用支付宝的支付接口
    # 支付宝信息  不能放在settings里 会报错
    app_private_key_string = open('testapp/keys/my_private_key.txt').read()
    alipay_public_key_string = open('testapp/keys/alipay_public_key.txt').read()
    print(alipay_public_key_string)
    alipay = AliPay(
        appid='2021000116684129',  # 沙箱应用id
        app_notify_url='http://127.0.0.1:8000/test/checkPay/',  # 默认回调的url
        app_private_key_string=app_private_key_string,  # 个人私钥
        alipay_public_key_string=alipay_public_key_string,  # 支付宝公钥
        sign_type='RSA2',  # 加密方式
        debug=True,  # 默认为False；True代表沙箱模式

    )

    # 获取扫码支付请求参数
    # 调用支付接口
    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string 实际地址
    # 沙箱地址 https://openapi.alipaydev.com/gateway.do? + order_string 沙箱地址在alipay后面加上dev
    order_string = alipay.api_alipay_trade_page_pay(
        subject='黒商人',
        out_trade_no=uuid.uuid4().hex,
        total_amount=str(amount),
        return_url='http://127.0.0.1:8000/test/checkPay/',
        notify_url='http://127.0.0.1:8000/test/checkPay/',  # 可选

    )

    response = alipay.api_alipay_trade_query(params.get('out_trade_no'))
    code = response.get('code')
    if code == '10000' and response.get('trade_status') == "TRADE_SUCCESS":

        return HttpResponse('支付成功！')
    return HttpResponse('支付失败！')
