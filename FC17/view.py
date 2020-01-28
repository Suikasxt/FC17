from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from FC17 import tools
from FC17.style import *
import json

def login(request):
	#如果从token和ID成功得到了用户信息，就记录进session
	if (request.POST and request.POST.get('token') and request.POST.get('ID')):
		userInfo, status_code = tools.getUserInfo(request.POST['token'], request.POST['ID'])
		if (status_code == 200):
			request.session['User'] = userInfo
			user = Users.objects.filter(id = userInfo['id'])
			if (len(user) == 0):
				user = Users(id = userInfo['id'])
			else:
				user = user[0]
			user.information = json.dumps(userInfo)
			user.save()
				
	return redirect("/")




def home(request):
	context = {}
	user = request.session.get('User')
	if (user):
		context['User'] = user
	return mainStyle(request, 'home.html', context)




def alert(request, output = 'test'):
	context = {}
	context['word'] = json.dumps(output)
	return render(request, 'alert.html', context)