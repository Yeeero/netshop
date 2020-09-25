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
from goods import views
from netshop.settings import DEBUG, MEDIA_ROOT

app_name = 'goods'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:cid>/', views.IndexView.as_view(), name='index'),
    path('category/<int:cid>/<int:pagenum>/', views.IndexView.as_view(), name='index'),
    path('goodsdetails/<int:goodsid>/', views.DetailView.as_view(), name='details'),
]

if DEBUG:
    from django.views.static import serve
    urlpatterns.append(re_path(r'media/(.*)', serve, kwargs={'document_root': MEDIA_ROOT}))
