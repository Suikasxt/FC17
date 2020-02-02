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
	try:
		if (request.POST and request.POST.get('token') and request.POST.get('ID')):
			result, status_code = tools.getUserInfoToken(request.POST['token'], request.POST['ID'])
		elif (request.POST and request.POST.get('username') and request.POST.get('ID') and request.POST.get('password')):
			result, status_code = tools.getUserInfoPassword(request.POST['username'], request.POST['ID'], request.POST['password'])
	except:
		result = 'System Error.'
	
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


def detail(request, userID = -1):
	user = request.session.get('User')
	res = {}
	if (user != None):
		if userID == -1:
			user = Users.objects.get(id = user['id'])
		else:
			user = Users.objects.get(id = userID)
		
		res = json.loads(user.information)
		del res['token']
		res['isCaptain'] = user.isCaptain
		res['isMember'] = user.isMember
		if (user.team):
			res['team'] = {
				'id' : user.team.id,
				'name' : user.team.name,
				'introduction' : user.team.introduction,
			}
			
	return HttpResponse(json.dumps(res), content_type = 'application/json')


def logout(request):
	try:
		del request.session['User']
		result = 'Logout successfully.'
	except:
		result = 'Nothing'
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')