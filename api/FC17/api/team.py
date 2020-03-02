from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import User
from FC17Website.models import Team
from FC17 import tools
from FC17 import view
import json

def list(request):
	teamList = Team.objects.all()
	result = []
	for team in teamList:
		result.append( {'id' : team.id, 'name' : team.name, 'introduction' : team.introduction} )
	return HttpResponse(json.dumps(result), content_type = 'application/json')



def detail(request, teamID = -1):
	user = tools.getCurrentUser(request)
	if (teamID == -1):
		if (user == None or user.isMember == False):
			return HttpResponse(json.dumps({}), content_type = 'application/json')
		else:
			team = user.team
	else:
		try:
			team = Team.objects.get(id = teamID)
		except:
			team = None
		
	if (team == None):
		return HttpResponse(json.dumps({'message': 'Team does\'t exist.', 'result': False}), content_type = 'application/json')
		
	members = User.objects.filter(team = team, isMember = True)
	result = { 'id' : team.id, 'name' : team.name, 'introduction' : team.introduction }
	memberList = []
	for member in members:
		info = json.loads(member.information)
		info = {'id': info['id'], 'username': info['username']}
		if member.isCaptain:
			captain = info
		else:
			memberList.append(info)
	result['members'] = memberList
	result['captain'] = captain
	
	if (user and captain and user.id == captain['id']):
		candidates = User.objects.filter(team = team, isMember = False)
		result['candidates'] = [{'id': user.id, 'username': json.loads(user.information)['username']} for user in candidates]
	result['result'] = True
	
	return HttpResponse(json.dumps(result), content_type = 'application/json')



def quit(request):
	user = tools.getCurrentUser(request)
	result = {}
	if (user == None):
		result['message'] = 'Please log in.'
		result['result'] = False
	elif (user.team == None):
		result['message'] = 'Not in a team now.'
		result['result'] = False
	elif (user.isCaptain == True):
		result['message'] = 'Captain can\'t quit.'
		result['result'] = False
	else:
		user.team = None
		if (user.isMember == True):
			user.isMember = False
			result['message'] = 'Quit successfully.'
			result['result'] = True
		else:
			result['message'] = 'Cancel successfully.'
			result['result'] = True
		user.save()
	return HttpResponse(json.dumps(result), content_type = 'application/json')



def apply(request, teamID):
	user = tools.getCurrentUser(request)
	team = Team.objects.get(id = teamID)
	result = {}
	if (team == None):
		result['message'] = 'Team does\'t exist.'
		result['result'] = False
	if (user == None):
		result['message'] = 'Please log in.'
		result['result'] = False
	elif (user.isMember):
		result['message'] = 'Already in a team now.'
		result['result'] = False
	else:
		user.team = team
		result['message'] = 'Apply successfully.'
		result['result'] = True
		user.save()
	return HttpResponse(json.dumps(result), content_type = 'application/json')



def manage(request):
	user = tools.getCurrentUser(request)
	result = {}
	if (user and user.isCaptain):
		team = user.team
		if (request.POST.get('name')):
			if len(request.POST['name']) > 30:
				return HttpResponse(json.dumps({'message': 'The name is too long', 'result': False}), content_type = 'application/json')
			team.name = request.POST['name']
		if (request.POST.get('introduction')):
			if len(request.POST['introduction']) > 250:
				return HttpResponse(json.dumps({'message': 'The introduction is too long', 'result': False}), content_type = 'application/json')
			team.introduction = request.POST['introduction']
		team.save()
		result['message'] = 'Update successfully'
		
		if (request.POST.get('accept')):
			result['message'] = 'Accept successfully'
			user = User.objects.get(id = request.POST['accept'])
			if (user and user.team == team):
				user.isMember = True
				user.save()
				
		if (request.POST.get('dismiss')):
			result['message'] = 'Dismiss successfully'
			user = User.objects.get(id = request.POST['dismiss'])
			if (user and user.team == team):
				user.isMember = False
				user.save()
		result['result'] = True
		
		if (request.POST.get('disband')):
			result['result'], result['message'] = tools.disbandTeam(team)
				
		
	elif (user and user.isMember == False and request.POST.get('name')):
		result['result'], result['message'] = tools.createTeam(user.id, request.POST.get('name'), request.POST.get('introduction'))
	else:
		result['message'] = 'Please log in.'
		result['result'] = False
	
	return HttpResponse(json.dumps(result), content_type = 'application/json')



def leaderboard(request):
	teamList = Team.objects.order_by('-score', 'id')
	result = []
	for index, team in enumerate(teamList):
		score = team.score
		teamInfo = {'rank' : index + 1, 'id' : team.id, 'name' : team.name, 'introduction' : team.introduction, 'score' : score}
		result.append(teamInfo)
		
	return HttpResponse(json.dumps(result), content_type = 'application/json')