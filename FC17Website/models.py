from django.db import models

class Teams(models.Model):
	name = models.CharField(max_length = 31, default = '')
	introduction = models.CharField(max_length = 255, default = '')

class Users(models.Model):
	id = models.IntegerField(primary_key=True)
	information = models.CharField(max_length = 1023, default = '')#以json字符串形式存储用户信息。登录时会进行更新。
	team = models.ForeignKey(to = Teams, on_delete = models.SET_NULL, null = True, related_name = 'belong_to')#isMember为否时表示申请加入该队伍
	isCaptain = models.BooleanField(default = False)#仅在队伍中且为队长是为真
	isMember = models.BooleanField(default = False)#在队伍中（包括队长）时为真

class Notices(models.Model):
	title = models.CharField(max_length = 255, default = '')
	content = models.CharField(max_length = 4095, default = '')

class Comments(models.Model):
	userID = models.ForeignKey(to = Users, on_delete = models.CASCADE)
	noticeID = models.ForeignKey(to = Notices, on_delete = models.CASCADE)
	content = models.CharField(max_length=4095, default = '')
	time = models.DateField(auto_now_add = True)
