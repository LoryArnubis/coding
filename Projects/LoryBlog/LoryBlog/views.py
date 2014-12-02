# -*- coding: utf-8 -*-
__author__ = 'wangweilong'

from django.shortcuts import render
from django.shortcuts import render_to_response

def first_page(request):
	context = {}
	context['label'] = 'Welcome to LoryBlog'
	return render_to_response('index.html')
	#return render_to_response(request, 'index.html', context)

