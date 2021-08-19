from django.contrib import admin
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'student', 'get_classe', 'school_fees', 'quran_ca', 'quran_exam', 'tajweed_ca',
    'tajweed_exam', 'mutoolaah_ca', 'mutoolaah_exam', 'arabiyyah_ca', 'arabiyyah_exam', 'nahw_ca',
    'nahw_exam', 'tawheed_ca', 'tawheed_exam', 'fiqh_ca', 'fiqh_exam', 'seeroh_ca', 'seeroh_exam',
    'hadeeth_ca', 'hadeeth_exam', 'cumulative']
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
