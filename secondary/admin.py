from django.contrib import admin
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'student', 'get_classe', 'school_fees', 'quran_ca', 'quran_exam', 'tajweed_ca',
    'tajweed_exam', 'nahw_ca', 'nahw_exam', 'sorf_ca', 'sorf_exam', 'uluum_ulquran_ca',
    'uluum_ulquran_exam', 'balaagah_ca', 'balaagah_exam', 'tawheed_ca', 'tawheed_exam',
    'farooid_ca', 'farooid_exam', 'fiqh_ca', 'fiqh_exam', 'taareekh_ca', 'taareekh_exam',
    'hadeeth_ca', 'hadeeth_exam', 'aruud_ca', 'aruud_exam', 'mantiqoh_ca', 'mantiqoh_exam',
    'tafseer_ca', 'tafseer_exam', 'mustolah_ulhadeeth_ca', 'mustolah_ulhadeeth_exam', 'cumulative']
    search_fields = ['student__user__username', 'student__classe__name']
    list_filter = ['student__classe__name']
    list_display_links = ['student']
    list_editable = ['school_fees']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.student.classe
    get_classe.admin_order_field = 'student'
    get_classe.short_description = 'Class'

admin.site.register(FirstTerm, FirstTermAdmin)
