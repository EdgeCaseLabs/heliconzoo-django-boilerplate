from django.contrib import admin
from models import *

class AuthTokenAdmin(admin.ModelAdmin):
    list_display	= ('user_id', 'session_id', 'token', 'created',)

admin.site.register(AuthToken, AuthTokenAdmin)
