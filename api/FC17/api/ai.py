from django.http import HttpResponse,StreamingHttpResponse
from FC17Website.models import User,AI
from FC17 import tools
from FC17.api.notice import DateEncoder
from FC17.settings import BASE_DIR
import os
import time
import json

SUFFIX='.cpp'

def upload(request):
    user = tools.getCurrentUser(request)
    res = {}
    print(request.POST['filename'])
    print(request.POST['description'])
    if user != None and request.method == 'POST' and request.POST.get('filename') and type(request.POST.get('description'))!=type(None):
        #limit the size and type of file to be uploaded
        myfile = request.FILES['file']
        if myfile:
            if myfile.size >= 1048576:
                res['error']=True
                res['message'] = 'Size of file should be less than 1MB.'
            elif myfile.name.endswith(SUFFIX) == False:
                res['error']=True
                res['message'] = 'Only {0} file will be accepted.'.format(SUFFIX)
            else:
                fileupload = AI()
                fileupload.filename = request.POST['filename']
                fileupload.user = user
                fileupload.team = user.team
                fileupload.description = request.POST['description']
                fileupload.file = myfile
                fileupload.save()
                print('Code uploaded. author={0}, name={1}'.format(user.id, fileupload.filename))

                res['error']=False
                res['message'] = 'You have successfully uploaded the code.'
        else:
            res['error']=True
            res['message'] = 'File does not exist.'
    elif user == None:
        res['error'] = True
        res['message'] = 'Please log in.'
    else:
        res['error'] = True
        res['message'] = 'Error'

    return HttpResponse(json.dumps(res), content_type = 'application/json')

def list(request):
    user = tools.getCurrentUser(request)
    res = {}
    if user:
        ai_list = AI.objects.filter(user = user)
        data=[]
        for ai in ai_list:
            #for attr in dir(ai.user):
            #    print(attr+":"+str(getattr(ai.user,attr)))
            data.append({
                'username' : json.loads(ai.user.information)["username"], 
                'filename' : ai.filename, 
                'description' : ai.description, 
                'upload time': ai.timestamp, 
                'ai id':ai.id
            })
        res['data']=data
        res['result']=True
    else:
        res['data']=[]
        res['result']=False
    return HttpResponse(json.dumps(res, cls=DateEncoder), content_type = 'application/json')

def list_team(request):
    user = tools.getCurrentUser(request)
    res = {}
    if user:
        ai_list = AI.objects.filter(team = user.team)
        data=[]
        for ai in ai_list:
            #for attr in dir(ai.user):
            #    print(attr+":"+str(getattr(ai.user,attr)))
            data.append({
                'username' : json.loads(ai.user.information)["username"], 
                'filename' : ai.filename, 
                'description' : ai.description, 
                'upload time': ai.timestamp, 
                'ai id':ai.id,
                'selected':ai.selected,
            })
        res['data']=data
        res['result']=True
    else:
        res['data']=[]
        res['result']=False
    return HttpResponse(json.dumps(res, cls=DateEncoder), content_type = 'application/json')

def get_file_path(file):
    return BASE_DIR.replace('\\','/')+'/FC17/media/'+file.path

def delete(request, pk):
    user = tools.getCurrentUser(request)
    res = {}
    if user:
        file = AI.objects.filter(id = pk)
        if len(file)==0:
            res['message']='File does not exist.'
            res['result']=False
        elif file[0].user!=user:
            res['message']='You can only delete your own file.'
            res['result']=False
        else:
            file = file[0]
            if os.path.exists(get_file_path(file)):
                os.remove(get_file_path(file))
            file.delete()
            res['message']='success'
            res['result']=True
    else:
        res['message']='Please login first.'
        res['result']=False
    return HttpResponse(json.dumps(res), content_type = 'application/json')

def select(request, pk):
    user = tools.getCurrentUser(request)
    res = {}
    if user:
        file = AI.objects.filter(id = pk)
        if len(file)==0:
            res['message']='File does not exist.'
            res['result']=False
        elif not file[0].team:
            res['message']='The file does not belong to a team.'
            res['result']=False
        elif file[0].team!=user.team:
            res['message']='You can only select file of your own team.'
            res['result']=False
        else:
            team = user.team
            team_files = AI.objects.filter(team = team)
            for f in team_files:
                f.selected=False
                f.save()
            file = file[0]
            file.selected = True
            file.save()
            res['message']='success'
            res['result']=True
    else:
        res['message']='Please login first.'
        res['result']=False
    return HttpResponse(json.dumps(res), content_type = 'application/json')

def filedownload(request ,pk):
    def file_iterator(file_name, chunk_size = 2048):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    user = tools.getCurrentUser(request)
    if user:
        file = AI.objects.filter(id = pk)
        if len(file)>0 and ((not file[0].team and file[0].user==user) or (file[0].team and file[0].team==user.team)):
            response = StreamingHttpResponse(file_iterator(get_file_path(file[0])))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file[0].origin_name)
    return response