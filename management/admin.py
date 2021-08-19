from django.contrib import admin
from .models import *

class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'next', 'head', 'school']
    search_fields = ['name']
    list_display_links = ['name', 'school']
    list_per_page = 10

admin.site.register(Session, SessionAdmin)
