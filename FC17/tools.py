import requests
import json

#根据token和ID获取
def getUserInfo(token, ID):
	headers = {'authorization' : 'Bearer token=' + str(token)}
	url = "https://api.eesast.com/v1/users/" + str(ID)
	res = requests.get(url, headers = headers)
	return json.loads(res.text), res.status_code
