from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type']
admin.site.register(Category, CategoryAdmin)

class AudioAdmin(admin.ModelAdmin):
    list_display = ['created', 'title', 'category', 'home_page', 'updated',  'audio']
    search_fields = ['title', 'created', 'updated']
    list_filter = ['home_page', 'category']
    list_display_links = ['title', 'audio']
    list_editable = ['home_page']
    list_per_page = 10

admin.site.register(Audio, AudioAdmin)
