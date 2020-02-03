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
	avatar = models.FileField(upload_to='avatars/', default="/avatars/default.png")
	adminLevel = models.IntegerField(default = 0)#管理员权限

class Notices(models.Model):
	author = models.ForeignKey(to = Users, on_delete = models.SET_NULL, null = True)
	time = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 255, default = '')
	content = models.CharField(max_length = 4095, default = '')

class Comments(models.Model):
	user = models.ForeignKey(to = Users, on_delete = models.CASCADE)
	notice = models.ForeignKey(to = Notices, on_delete = models.CASCADE)
	content = models.CharField(max_length = 4095, default = '')
	time = models.DateTimeField(auto_now_add = True)
