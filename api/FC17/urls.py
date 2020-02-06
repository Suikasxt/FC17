"""FC17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from FC17 import settings
from FC17 import view
from FC17 import team
from FC17 import notice
from FC17.api import user as api_user
from FC17.api import team as api_team
from FC17.api import notice as api_notice
from FC17.api import ai as api_ai

urlpatterns = [
	url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
	
    path('admin/', admin.site.urls),
    path('test/', view.alert),
    path('login/', view.login),
    path('logout/', view.logout),
    path('notice/', notice.list),
    path('notice/create/', notice.create),
    path('notice/<int:noticeID>/', notice.detail),
    path('team/', team.detail),
    path('team/<int:teamID>/', team.detail),
    path('team/list/', team.list),
    path('team/manage/', team.manage),
    path('', view.home),
	
    path('api/user/login/', api_user.login),
    path('api/user/<int:userID>/', api_user.detail),
    path('api/user/', api_user.detail),
    path('api/user/logout/', api_user.logout),
    path('api/user/update/', api_user.update),
    path('api/team/list/', api_team.list),
    path('api/team/leaderboard/<str:type>/', api_team.leaderboard),
    path('api/team/', api_team.detail),
    path('api/team/<int:teamID>/', api_team.detail),
    path('api/team/quit/', api_team.quit),
    path('api/team/apply/<int:teamID>', api_team.apply),
    path('api/team/manage/', api_team.manage),
    path('api/notice/list/', api_notice.list),
    path('api/ai/upload/', api_ai.upload),
    path('api/ai/list/', api_ai.list),
    path('api/ai/delete/<int:pk>/', api_ai.delete),
    path('api/ai/list_team/', api_ai.list_team),
    path('api/ai/select/<int:pk>/', api_ai.select),
    path('api/ai/download/<int:pk>/', api_ai.filedownload),
]
