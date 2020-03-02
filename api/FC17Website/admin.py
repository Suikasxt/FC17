from django.contrib import admin
from FC17Website.models import Team,Notice,Comment,AI,AI_test
# Register your models here.
admin.site.register(Team)
admin.site.register(Notice)
admin.site.register(Comment)
admin.site.register(AI)
admin.site.register(AI_test)