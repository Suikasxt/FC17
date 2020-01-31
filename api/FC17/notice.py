from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from FC17Website.models import Notices
from FC17Website.models import Comments
from FC17 import tools
from FC17 import view
import json

def list(request):
	noticeList = Notices.objects.all()
	context = {'noticeList' : noticeList}
	return view.mainStyle(request, 'notice/list.html', context)


def detail(request, noticeID):
	user = request.session.get('User')
	notice = Notices.objects.get(id = noticeID)
	
	context = {'notice' : notice}
	
	if (notice == None):
		return view.alert("The notice doesn't exist.")
	
	if (request.POST and request.POST.get('comment') and user):
		result, tips = tools.submitComment(user['id'], request.POST['comment'], notice)
		context['result'] = result
		context['tips'] = tips
	
	
	commentList = Comments.objects.filter(notice = notice)
	commentListWithUser = []
	for comment in commentList:
		commentListWithUser.append({'comment' : comment, 'user' : json.loads(comment.user.information)})
	context['commentList'] = commentListWithUser
	return view.mainStyle(request, 'notice/detail.html', context)


def create(request):
	user = request.session.get('User')
	if (user == None):
		return view.alert(request, 'Please login!')
	else:
		user = Users.objects.get(id = user['id'])
		if (user == None or user.adminLevel == 0):
			return view.alert(request, 'Your level is not enough!')
	
	if (request.POST and request.POST.get('title') and request.POST.get('content')):
		result, tips = tools.createNotice(user, request.POST['title'], request.POST['content'])
		return view.alert(request, tips)
		
	return view.mainStyle(request, 'notice/create.html')