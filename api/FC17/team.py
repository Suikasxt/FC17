from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import User
from FC17Website.models import Team
from FC17 import tools
from FC17 import view
import json


#队长管理队伍
def manage(request):
	user = request.session.get('User')
	if (user == None):
		return view.alert(request, 'Please login!')
	
	user = User.objects.get(id = user['id'])
	
	if (user.isCaptain == False):
		return view.alert(request, 'You are not a captain.')
	
	context = { 'team' : user.team }
	
	#通过入队申请
	if (request.POST and request.POST.get('accept')):
		candidate = User.objects.get(id = request.POST.get('accept'))
		if (candidate and candidate.team == user.team and candidate.isMember == False):
			candidate.isMember = True
			candidate.save()
	
	candidateList = User.objects.filter(team = user.team, isMember = False)
	context['candidateList'] = []
	for candidate in candidateList:
		context['candidateList'].append(json.loads(candidate.information))
	return view.mainStyle(request, 'team/manage.html', context)
	


def create(request):
	user = request.session.get('User')
	if (user == None):
		return view.alert(request, 'Please login!')
		
	context = {}
	if (request.POST and request.POST.get('name') and request.POST.get('introduction')):
		result, tips = tools.createTeam(user['id'], request.POST['name'], request.POST['introduction'])
		#result 为True/False表示是否创建成功，tips为相应提示
		context['result'] = result
		context['tips'] = tips
		return detail(request)
	return view.mainStyle(request, 'team/create.html', context)




def detail(request, teamID = None):
	user = request.session.get('User')
	if (user != None):
		user = User.objects.get(id = user['id'])
	
	
	
	if (teamID):
		team = Team.objects.get(id = teamID)
		if (team == None):
			return view.alert("Team doesn't exist")
		if (user and request.POST):
			if (user.isMember == 0 and request.POST.get('action') == 'Join'):
				user.team = team
				user.save()
			elif team == user.team:
				if (user.isCaptain == 0 and request.POST.get('action') == 'Exit'):
					user.team = None
					user.isMember = 0
					user.save()
				elif (user.isCaptain == 1 and request.POST.get('action') == 'Disband'):
					tools.disbandTeam(team)
					return redirect("/team/")
	else:
		if (user == None):
			return view.alert(request, 'Please login!')
	
		if (user.isMember == False):
			return create(request)
		else:
			team = user.team
		
		
		
	context = {'team' : team}
	memberList = []
	members = User.objects.filter(team = team, isMember = True)
	
	for member in members:
		if member.isCaptain:
			captain = json.loads(member.information)
		else:
			memberList.append(json.loads(member.information))
	context['members'] = memberList
	context['captain'] = captain
	context['user'] = user
	return view.mainStyle(request, 'team/detail.html', context)




def list(request):
	teamList = Team.objects.all()
	context = {'teamList' : teamList}
	return view.mainStyle(request, 'team/list.html', context)