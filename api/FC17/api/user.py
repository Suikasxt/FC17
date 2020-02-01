from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from FC17Website.models import Teams
from FC17 import tools
from FC17 import view
import json

def login(request):
	
	result = "Data missing."
	status_code = 0
	#如果从token和ID成功得到了用户信息，就记录进session
	if (request.POST and request.POST.get('token') and request.POST.get('ID')):
		result, status_code = tools.getUserInfoToken(request.POST['token'], request.POST['ID'])
	elif (request.POST and request.POST.get('username') and request.POST.get('ID') and request.POST.get('password')):
		result, status_code = tools.getUserInfoPassword(request.POST['username'], request.POST['ID'], request.POST['password'])
	
	if (status_code == 200):
		if (request.POST.get('remember') != 'true'):
			request.session.set_expiry(0)
		request.session['User'] = result
		user = Users.objects.filter(id = result['id'])
		if (len(user) == 0):
			user = Users(id = result['id'])
		else:
			user = user[0]
		user.information = json.dumps(result)
		user.save()
		result = {'message' : 'Login successfully', 'result' : 1}
	else:
		result = {'message' : result, 'result' : 0}
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')
	'''response.setHeader("Access-Control-Allow-Origin", request.getHeader("Origin"));
	response.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE");
	response.setHeader("Access-Control-Max-Age", "0");
	response.setHeader("Access-Control-Allow-Headers", "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With,userId,token,Access-Control-Allow-Headers");
	response.setHeader("Access-Control-Allow-Credentials", "true");
	response.setHeader("XDomainRequestAllowed","1");
	return response'''


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


def logout(request):
	try:
		del request.session['User']
		result = 'Logout successfully.'
	except:
		result = 'Nothing'
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')