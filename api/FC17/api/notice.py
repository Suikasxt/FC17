from FC17Website.models import Notice
from django.http import HttpResponse
import json
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)

def list(request):
    noticeList = Notice.objects.all()
    result = []
    for n in noticeList:
        print(n.time)
        result.append( {'time' : n.time, 'title' : n.title, 'content' : n.content} )
    return HttpResponse(json.dumps(result, cls=DateEncoder), content_type = 'application/json')
	