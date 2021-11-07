from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['category']
=======
    list_display = ['type']
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
admin.site.register(Category, CategoryAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['created', 'title', 'category', 'home_page', 'updated',  'video']
    search_fields = ['title', 'created', 'updated']
    list_filter = ['home_page', 'category']
    list_display_links = ['title', 'video']
    list_editable = ['home_page']
    list_per_page = 10

admin.site.register(Video, VideoAdmin)
