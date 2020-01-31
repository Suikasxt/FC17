import requests
import json
from FC17Website.models import Users
from FC17Website.models import Teams
from FC17Website.models import Notices
from FC17Website.models import Comments
server = 'https://api.eesast.com'

def submitComment(userID, content, notice):
	if userID == None:
		return False, "User doesn't exist!"
	user = Users.objects.get(id = userID)
	if user == None:
		return False, "User doesn't exist!"
	
	comment = Comments(user = user, content = content, notice = notice)
	comment.save()
	return True, "Submit successfully!"

def createNotice(author, title, content):
	if (author.adminLevel == 0):
		return False, 'Your level is not enough!'
	notice = Notices(author = author, title = title, content = content)
	notice.save()
	return True, "Create successfully!"

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
def getUserInfoToken(token, ID):
	headers = {'authorization' : 'Bearer token=' + str(token)}
	url = server + "/v1/users/" + str(ID)
	res = requests.get(url, headers = headers)
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
def getUserInfoPassword(username, ID, password):
	data = {'username' : username, 'password' : password}
	url = server + "/v1/users/login"
	print(url, data)
	res = requests.post(url, data = data)
	if res.status_code != 200:
		return "Invalid ID and password", res.status_code
	token = json.loads(res.text)['token']
	return getUserInfoToken(token, ID)