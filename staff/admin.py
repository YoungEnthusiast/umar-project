from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

admin.site.register(Teacher, TeacherAdmin)
