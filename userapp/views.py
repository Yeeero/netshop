from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
# Create your views here.
from django.views.generic.base import View

from userapp.forms import LoginForm
from userapp.models import *


# 装饰器，用户登录状态验证,未登录用户跳转到登录页面
def checkLogin(params=None):        # param => next, 登录后需要跳转的url
    def inner(func):
        def wrapper(obj, request, *args, **kwargs):
            print(params)
            if request.session.get('user'):
                return func(obj, request, *args, **kwargs)
            return redirect('/user/login/?next={}'.format(params))
        return wrapper
    return inner



class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        try:
            user = UserInfo.objects.create(uname=username, pwd=password)
        except Exception:
            return redirect(reverse('user:register'))
        request.session['user'] = user
        return redirect(reverse('user:center'))


# Ajax 验证注册用户
class CheckUsername(View):
    def get(self, request):
        uname = request.GET.get('uname')
        if UserInfo.objects.filter(uname=uname):
            return JsonResponse({'flag': True})
        else:
            return {'flag': False}


class CenterView(View):
    @checkLogin
    def get(self, request):
        return render(request, 'center.html')


class LogoutView(View):
    def get(self, request):
        if 'user' in request.session:
            del request.session['user']
        return redirect(reverse('goods:index'))

    def post(self, request):
        # 删除session中登录用户信息
        if 'user' in request.session:
            del request.session['user']

        return JsonResponse({'delflag': True})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        next = request.GET.get('next')  # 获取跳转页面的url
        print('----get---->next=', next)
        return render(request, 'login.html', locals())

    def post(self, request):
        form = LoginForm()
        # print(request.POST)
        validata = LoginForm(request.POST)
        print('validata = ', validata.errors)
        print('---->', validata.is_valid())
        if validata.errors:
            return render(request, 'login.html', locals())
        print('-' * 30)
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        next = request.POST.get('next')  # 获取跳转页面的url
        print('next =', next)
        print('pwd = ', pwd)
        userlist = UserInfo.objects.filter(uname=uname, pwd=pwd)
        cleanData = validata.cleaned_data
        if userlist:
            request.session['user'] = userlist[0]
            try:
                return redirect(next)
            except:
                return redirect('user:center')
        else:
            return render(request, 'login.html', {'msg': '用户不存在或密码不正确', 'form': form})


# 刷新验证码
def refresh(request):
    form = LoginForm()
    return render(request, 'login.html', context=locals())


class AddressView(View):
    @checkLogin
    def get(self, request):
        user = request.session.get('user')
        addresslist = Address.objects.filter(userinfo=user)
        return render(request, 'address.html', locals())

    def post(self, request):
        aname = request.POST.get('aname')
        aphone = request.POST.get('aphone')
        addr = request.POST.get('addr')
        user = request.session.get('user')
        print(aname, '-', aphone, '-', addr)
        address = Address.objects.create(aname=aname, aphone=aphone, addr=addr, userinfo=user,
                               isdefault=(lambda count: True if count == 0 else False)(user.address_set.all().count()))
        return render(request, 'address.html', locals())


class LoadAreaView(View):
    def get(self, request):
        print('---' * 10)
        pid = request.GET.get('pid', 0)
        pid = int(pid)
        # 根据pid查询区划信息
        areas = Areas.objects.filter(pid=pid)
        # 序列化
        jarealist = serialize('json', areas)
        return JsonResponse({'jarealist': jarealist})


class SetDefaultAddrView(View):
    def get(self, request):
        print('-------setdefaultaddr-------')
        user = request.session.get('user')
        data = request.GET.dict()
        print(request.GET.dict())
        addresslist = Address.objects.filter(userinfo=user)
        for address in addresslist:
            address.isdefault = False
            address.save()
        address2 = Address.objects.get(userinfo=user, **data)
        address2.isdefault = True
        address2.save()
        return JsonResponse({"msg": True})


class DeleteAddrView(View):
    def get(self, request):
        data = request.GET.dict()
        user = request.session.get('user')
        address = Address.objects.get(userinfo=user, **data)
        address.delete()
        return JsonResponse({"msg": 'delete'})