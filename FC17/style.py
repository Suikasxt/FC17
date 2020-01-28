from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from FC17Website.models import Users
from . import tools
import json


#用于统一页面风格
def mainStyle(request, content = "home.html", context = {}):
	return render(request, content, context)
