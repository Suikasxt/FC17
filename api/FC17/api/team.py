from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from FC17Website.models import Teams
from FC17 import tools
from FC17 import view
import json

def list(request):
	teamList = Teams.objects.all()
	result = []
	for team in teamList:
		result.append( {'id' : team.id, 'name' : team.name, 'introduction' : team.introduction} )
	return HttpResponse(json.dumps(result), content_type = 'application/json')
	
def detail(request, teamID = -1):
	user = tools.getCurrentUser(request)
	if (teamID == -1):
		if (user == None):
			result = None
		else:
			result = user.team
	else:
		result = Teams.objects.get(id = teamID)
	
	members = Users.objects.filter(team = result, isMember = True)
	result = { 'name' : result.name, 'introduction' : result.introduction}
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
	
	return HttpResponse(json.dumps(result), content_type = 'application/json')