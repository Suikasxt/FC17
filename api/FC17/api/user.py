from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from FC17Website.models import Teams
from FC17 import tools
from FC17 import view
import json

def login(request):
	try:
		del request.session['User']
	except:
		pass
	
	result = "Data missing."
	#如果从token和ID成功得到了用户信息，就记录进session
	if (request.POST and request.POST.get('token') and request.POST.get('ID')):
		result, status_code = tools.getUserInfoToken(request.POST['token'], request.POST['ID'])
	elif (request.POST and request.POST.get('username') and request.POST.get('ID') and request.POST.get('password')):
		result, status_code = tools.getUserInfoPassword(request.POST['username'], request.POST['ID'], request.POST['password'])
	
	if (status_code == 200):
		request.session['User'] = result
		user = Users.objects.filter(id = result['id'])
		if (len(user) == 0):
			user = Users(id = result['id'])
		else:
			user = user[0]
		user.information = json.dumps(result)
		user.save()
		result = {'message' : 'Login successfully', 'result' : 1}
	
	result = {'message' : result, 'result' : 0}
	return HttpResponse(json.dumps(result), content_type = 'application/json')

def detail(request, userID = -1):
	user = request.session.get('User')
	if (user != None):
		if userID == -1:
			user = Users.objects.get(id = user['id'])
		else:
			user = Users.objects.get(id = userID)
		return HttpResponse(user.information, content_type = 'application/json')
	else:
		return HttpResponse('{}', content_type = 'application/json')