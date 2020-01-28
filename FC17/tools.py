import requests
import json
from FC17Website.models import Users
from FC17Website.models import Teams

def createTeam(userID, teamName = 'Unnamed', introduction = ''):
	user = Users.objects.get(id = userID)
	if (user == None):
		return False, 'System error!'
		
	if (user.isMember):
		return False, 'Already in a Team!'
	
	if (teamName == ''):
		return False, 'Teamname should not be empty.'
	
	team = Teams(name = teamName, introduction = introduction)
	team.save()
	user.team = team
	user.isMember = True
	user.isCaptain= True
	user.save()
	return True, 'Create successfully.'

#根据token和ID获取
def getUserInfo(token, ID):
	headers = {'authorization' : 'Bearer token=' + str(token)}
	url = "https://api.eesast.com/v1/users/" + str(ID)
	res = requests.get(url, headers = headers)
	return json.loads(res.text), res.status_code
