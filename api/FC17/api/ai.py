from django.http import HttpResponse
import json
from FC17Website.models import User,AI
from FC17 import tools
import time
from FC17.api.notice import DateEncoder

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
    ai_list = AI.objects.filter(user = user)
    result = []
    for ai in ai_list:
        result.append( {'username' : ai.user.username, 'filename' : ai.filename, 'description' : ai.description, 'upload time': ai.timestamp} )
    return HttpResponse(json.dumps(result, cls=DateEncoder), content_type = 'application/json')