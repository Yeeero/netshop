# -*- coding = utf-8 -*-
# @Time :
# @ Author : Yeeero
# @File : mycontextprocessors.by
# @Software : PyCharm
'''
    全局上下文
'''


def getUserInfo(request):
    return {'suser': request.session.get('user')}
