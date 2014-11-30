# -*- coding: utf-8 -*-
__author__ = 'wangweilong'

from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>hello world</p>")
