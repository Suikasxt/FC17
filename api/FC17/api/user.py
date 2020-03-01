from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import User
from FC17Website.models import Team
from FC17 import tools
from FC17 import view
import json

def login(request):
	
	result = "Data missing."
	status_code = 0
	#如果从token和ID成功得到了用户信息，就记录进session
	try:
		if (request.POST and request.POST.get('token')):
			result, status_code = tools.getUserInfoToken(request.POST['token'])
		elif (request.POST and request.POST.get('username') and request.POST.get('password')):
			result, status_code = tools.getUserInfoPassword(request.POST['username'], request.POST['password'])
	except:
		result = 'System Error.'
	
	if (status_code == 200):
		if (request.POST.get('remember') != 'true'):
			request.session.set_expiry(0)
		request.session['User'] = result
		user = User.objects.filter(id = result['id'])
		if (len(user) == 0):
			user = User(id = result['id'])
		else:
			user = user[0]
		user.information = json.dumps(result)
		user.save()
		result = {'message' : 'Login successfully', 'result' : True}
	else:
		result = {'message' : result, 'result' : False}
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')


def detail(request, userID = -1):
	user = request.session.get('User')
	res = {}
	if (user != None):
		if userID == -1:
			user = User.objects.get(id = user['id'])
		else:
			user = User.objects.get(id = userID)
		
		res = json.loads(user.information)
		del res['token']
		res['isCaptain'] = user.isCaptain
		res['isMember'] = user.isMember
		res['avatar'] = str(user.avatar)
		if (user.team):
			res['team'] = {
				'id' : user.team.id,
				'name' : user.team.name,
				'introduction' : user.team.introduction,
			}
			
	return HttpResponse(json.dumps(res), content_type = 'application/json')

def update(request):
	user = tools.getCurrentUser(request)
	if (user == None):
		return HttpResponse(json.dumps({'message': 'Please log in.'}), content_type = 'application/json')
		
	changes = {}
	return HttpResponse(json.dumps(changes), content_type = 'application/json')

def logout(request):
	try:
		del request.session['User']
		result = {'message': 'Logout successfully.', 'result': True}
	except:
		result = {'message': 'Nothing', 'result': False}
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')