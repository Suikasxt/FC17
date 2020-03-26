import os
import csv
import codecs
import zipfile
import hashlib
from FC17 import settings
from django.contrib import admin
from django.http import HttpResponse
from FC17Website.models import Team,Notice,Comment,AI,AI_test,User


def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

def Download_Selected(modeladmin, request, queryset):
	zipPath = settings.MEDIA_ROOT + 'files.zip'
	csvPath = settings.MEDIA_ROOT + 'fileinfo.csv'
	zip = zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED)
	csvFile = open(csvPath, 'w', newline='')
	csvWriter = csv.writer(csvFile)
	csvWriter.writerow(('ID', 'Name', 'TeamID', 'TeamName', 'Filename', 'MD5'))
	for ai in queryset:
		aiPath = os.path.join(settings.MEDIA_ROOT, ai.path)
		zip.write(aiPath, ai.path)
		csvWriter.writerow((ai.id, ai.filename, ai.team.id, ai.team.name, ai.exact_name, GetFileMd5(aiPath)))
	zip.write(csvPath, 'fileinfo.csv')
	zip.close()
	csvFile.close()
	
	def readFile(fn, buf_size=262144):
		f = open(fn, "rb")
		while True:
			c = f.read(buf_size)
			if c:
				yield c
			else:
				break
		f.close()
	respone = HttpResponse(readFile(zipPath), content_type='application/octet-stream')
	respone['Content-Disposition'] = 'attachment; filename=files.zip'
	return respone
Download_Selected.short_description = "Download files selected"

class aiAdmin(admin.ModelAdmin):
	actions = [Download_Selected]
	search_fields = ('selected',)
	
class userAdmin(admin.ModelAdmin):
	search_fields = ('isMember',)
	
admin.site.register(Team)
admin.site.register(Notice)
admin.site.register(Comment)
admin.site.register(User, userAdmin)
admin.site.register(AI, aiAdmin)
admin.site.register(AI_test)
