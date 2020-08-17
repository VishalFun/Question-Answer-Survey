from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Task'

admin.site.register(models.Choices)
admin.site.register(models.UserInfo)
admin.site.register(models.Question)
admin.site.register(models.UserResponse)
