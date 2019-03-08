# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 0009 1:49
# @Author  : __Yanfeng
# @Site    : 
# @File    : counttime.py
# @Software: PyCharm
import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('student:index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        return response
