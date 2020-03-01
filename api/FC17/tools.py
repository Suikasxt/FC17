import requests
import json
from FC17Website.models import User
from FC17Website.models import Team
from FC17Website.models import Notice
from FC17Website.models import Comment
server = 'https://api.eesast.com'

def submitComment(userID, content, notice):
	if userID == None:
		return False, "User doesn't exist!"
	user = User.objects.get(id = userID)
	if user == None:
		return False, "User doesn't exist!"
	
	comment = Comment(user = user, content = content, notice = notice)
	comment.save()
	return True, "Submit successfully!"

def createNotice(author, title, content):
	if (author.adminLevel == 0):
		return False, 'Your level is not enough!'
	notice = Notice(author = author, title = title, content = content)
	notice.save()
	return True, "Create successfully!"

def createTeam(userID, teamName = 'Unnamed', introduction = ''):
	user = User.objects.get(id = userID)
	if (user == None):
		return False, 'System error!'
		
	if (user.isMember):
		return False, 'Already in a Team!'
	
	if (teamName == ''):
		return False, 'Teamname should not be empty.'
	
	if (introduction == None):
		introduction = ''
	
	team = Team(name = teamName, introduction = introduction)
	team.save()
	user.team = team
	user.isMember = True
	user.isCaptain= True
	user.save()
	return True, 'Create successfully.'
	
def disbandTeam(team):
	if (team == None):
		return False, 'Team doesn\'t exist.'
	User.objects.filter(team = team).update(team = None, isMember = False, isCaptain = False)
	team.delete()
	return True, 'Disband successfully.'

#根据token和ID获取
def getUserInfoToken(token):
	headers = {"Content-Type": "application/json"}
	data = {'token' : str(token)}
	url = server + "/v1/users/token/validate/"
	res = requests.post(url, data = json.dumps(data), headers = headers)
	if (res.status_code != 200):
		result = 'Token not available.'
	else:
		try:
			result = json.loads(res.text)
			result['token'] = token
		except:
			result = 'System Error'
	return result, res.status_code


#根据username和password获取
def getUserInfoPassword(username, password):
	data = {'username' : username, 'password' : password}
	url = server + "/v1/users/login"
	headers = {"Content-Type": "application/json"} 
	
	res = requests.post(headers = headers, url = url, data = json.dumps(data))
	if res.status_code != 200:
		return "Invalid ID and password", res.status_code
	token = json.loads(res.text)['token']
	return getUserInfoToken(token)

def getCurrentUser(request):
	try:
		return User.objects.get(id = request.session.get('User')['id'])
	except:
		return None