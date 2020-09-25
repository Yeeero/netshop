"""netshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#coding=utf-8

from django.contrib import admin
from django.urls import path, re_path, include
import goods
from userapp import views
from netshop.settings import DEBUG, MEDIA_ROOT

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('checkuname/', views.CheckUsername.as_view(), name='checkuname'),
    path('center/', views.CenterView.as_view(), name='center'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('refresh/', views.refresh, name='refresh'),       # 刷新验证码
    path('address/', views.AddressView.as_view(), name='address'),
    path('loadarea/', views.LoadAreaView.as_view(), name='loadarea'),
    path('setdefaultaddr/', views.SetDefaultAddrView.as_view(), name='setdefaultaddr'),
    path('deleteaddr/', views.DeleteAddrView.as_view(), name='deleteaddr'),

]

if DEBUG:
    from django.views.static import serve
    urlpatterns.append(re_path(r'media/(.*)', serve, kwargs={'document_root': MEDIA_ROOT}))
