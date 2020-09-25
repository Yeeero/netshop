# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : forms.by
# @Software : PyCharm

# 登录验证，验证码
from captcha.fields import CaptchaField
from django import forms


class LoginForm(forms.Form):
    uname = forms.CharField(min_length=6, required=True)
    pwd = forms.CharField(required=True, min_length=4, error_messages={
        'required': '密码必须填写',
        'min_length': '密码不能小于4位',
    })
    # 验证码使用， error_massage修改错误提示信息
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})