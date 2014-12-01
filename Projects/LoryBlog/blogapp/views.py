# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render

from blogapp.models import Character

def first_page(request):
	context = {}
	context['label'] = 'blogapp'
	return render(request, 'templay.html', context)

def staff(request):
	staff_list = Character.objects.all()
	#staff_str = map(str, staff_list)
	#context = {'label': ' '.join(staff_str)}
	return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
	context = {}
	context['label'] = 'Hello World'
	return render(request, 'templay.html', context)
