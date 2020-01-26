from django.http import HttpResponse
from django.shortcuts import render
from . import tools
import json


def login(request):
	#如果从token和ID成功得到了用户信息，就记录进session
	if (request.POST and request.POST['token']):
		userInfo, status_code = tools.getUserInfo(request.POST['token'], request.POST['ID'])
		if (status_code == 200):
			request.session['User'] = userInfo
	return home(request)
	
def home(request):
	context = {}
	userInfo = request.session.get('User')
	if (userInfo):
		context['User'] = userInfo
	return render(request, 'home.html', context)
	
def test(request, output = 'test'):
	context = {}
	context['word'] = json.dumps(output)
	return render(request, 'test.html', context)