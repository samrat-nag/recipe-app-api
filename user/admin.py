from django.contrib import admin
from user import models
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#from core import models

#class UserAdmin(BaseUserAdmin):
#    ordering =['id']
#    list_display =['email','name']

#admin.site.register(models.User,UserAdmin)
admin.site.register(models.UserProfileFeedItem)

# Register your models here.
