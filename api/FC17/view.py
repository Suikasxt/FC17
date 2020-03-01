from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import User
from FC17.api import user as api_user
from FC17 import tools
import json


#用于统一页面风格
def mainStyle(request, content = "home.html", context = {}):
	user = request.session.get('User')
	if (user != None):
		user = User.objects.get(id = user['id'])
		context['User'] = user
		context['UserInformation'] = json.loads(user.information)
	
	return render(request, content, context)

def login(request):
	status_code = 0
	#如果从token和ID成功得到了用户信息，就记录进session
	if (request.POST and request.POST.get('token')):
		result, status_code = tools.getUserInfoToken(request.POST['token'])
	elif (request.POST and request.POST.get('username') and request.POST.get('password')):
		result, status_code = tools.getUserInfoPassword(request.POST['username'], request.POST['password'])
	
	if (status_code == 200):
		request.session['User'] = result
		user = User.objects.filter(id = result['id'])
		if (len(user) == 0):
			user = User(id = result['id'])
		else:
			user = user[0]
		user.information = json.dumps(result)
		user.save()
				
	return redirect("/")




def home(request):
	return mainStyle(request, 'home.html')



def alert(request, output = 'test'):
	context = {}
	context['word'] = json.dumps(output)
	return mainStyle(request, 'alert.html', context)

def logout(request):
	return api_user.logout(request)