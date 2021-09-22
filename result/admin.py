from django.contrib import admin
from .models import First

class FirstAdmin(admin.ModelAdmin):
    list_display = ['session', 'value', 'student', 'school_fees', 'static_class', 'get_classe', 'subject', 'ca1', 'ca2', 'exam', 'total', 'subject_total', 'subject_avg', 'subject_pos', 'grade', 'cumulative', 'cum_perc', 'created', 'updated']
    search_fields = []
    list_filter = ['subject', 'student__classe']
    list_display_links = ['student']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.student.classe
    get_classe.admin_order_field = 'Student'
    get_classe.short_description = 'Class'

admin.site.register(First, FirstAdmin)
