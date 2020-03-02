from django.db import models
import random
import os
import time

class Team(models.Model):
	name = models.CharField(max_length = 31, default = '')
	introduction = models.CharField(max_length = 255, default = '')
	score = models.IntegerField(default = 0)

class User(models.Model):
	id = models.IntegerField(primary_key=True)
	information = models.CharField(max_length = 1023, default = '')#以json字符串形式存储用户信息。登录时会进行更新。
	team = models.ForeignKey(to = Team, on_delete = models.SET_NULL, null = True, related_name = 'belong_to')#isMember为否时表示申请加入该队伍
	isCaptain = models.BooleanField(default = False)#仅在队伍中且为队长是为真
	isMember = models.BooleanField(default = False)#在队伍中（包括队长）时为真
	avatar = models.FileField(upload_to='avatars/', default="/avatars/default.png")
	adminLevel = models.IntegerField(default = 0)#管理员权限

class Notice(models.Model):
	author = models.ForeignKey(to = User, on_delete = models.SET_NULL, null = True)
	time = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 255, default = '')
	content = models.CharField(max_length = 4095, default = '')

class Comment(models.Model):
	user = models.ForeignKey(to = User, on_delete = models.CASCADE)
	notice = models.ForeignKey(to = Notice, on_delete = models.CASCADE)
	content = models.CharField(max_length = 4095, default = '')
	time = models.DateTimeField(auto_now_add = True)

def user_dirpath(instance, filename):
	now = time.strftime('%Y%m%d%H%M%S')
	exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), filename)
	while os.path.exists('fileupload/{0}'.format(exact_name)):
		exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), filename)
	_path = 'fileupload/{0}'.format(exact_name)
	instance.path = _path
	instance.origin_name = filename
	instance.exact_name = exact_name
	return './' + _path

class AI(models.Model):
	filename = models.CharField(max_length = 255)
	user = models.ForeignKey(to = User, on_delete = models.CASCADE, null = True)
	team = models.ForeignKey(to = Team, on_delete = models.CASCADE, null = True)
	description = models.CharField(max_length = 1000, null = True, blank = True, default = '')
	file = models.FileField(upload_to = user_dirpath)
	path = models.CharField(max_length = 500)
	origin_name = models.CharField(max_length = 255, default = filename) #原文件名
	exact_name = models.CharField(max_length = 255, default = origin_name) #所存文件名
	timestamp = models.DateTimeField(auto_now_add = True)
	selected = models.BooleanField(default = False)
	rank_daily = models.IntegerField(default = 0) #日榜排名
	rank_overall = models.IntegerField(default = 0) #总榜排名
	score = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.filename

	class Meta:
		verbose_name = 'FileInfo'
		ordering = ['-timestamp']

def user_dirpath_test(instance, filename):
	now = time.strftime('%Y%m%d%H%M%S')
	exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), filename)
	while os.path.exists('fileupload_test/{0}'.format(exact_name)):
		exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), filename)
	_path = 'fileupload_test/{0}'.format(exact_name)
	instance.path = _path
	instance.origin_name = filename
	instance.exact_name = exact_name
	return './' + _path

class AI_test(models.Model):
	filename = models.CharField(max_length = 255)
	team_name = models.CharField(max_length=512)
	team_mate1 = models.CharField(max_length=512)
	team_mate2 = models.CharField(max_length=512)
	team_mate3 = models.CharField(max_length=512)
	description = models.CharField(max_length = 1000, null = True, blank = True, default = '')
	file = models.FileField(upload_to = user_dirpath_test)
	path = models.CharField(max_length = 500)
	origin_name = models.CharField(max_length = 255, default = filename) #原文件名
	exact_name = models.CharField(max_length = 255, default = origin_name) #所存文件名
	timestamp = models.DateTimeField(auto_now_add = True)
	selected = models.BooleanField(default = False)
	rank_daily = models.IntegerField(default = 0) #日榜排名
	rank_overall = models.IntegerField(default = 0) #总榜排名
	score = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.filename

	class Meta:
		verbose_name = 'FileInfo_test'
		ordering = ['-timestamp']
