from django.contrib import admin
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'pupil', 'get_classe', 'school_fees', 'quran_ca', 'quran_exam', 'tajweed_ca',
    'tajweed_exam', 'mutoolaah_ca', 'mutoolaah_exam', 'arabiyyah_ca', 'arabiyyah_exam', 'nahw_ca',
    'nahw_exam', 'tawheed_ca', 'tawheed_exam', 'fiqh_ca', 'fiqh_exam', 'seeroh_ca', 'seeroh_exam',
    'hadeeth_ca', 'hadeeth_exam', 'imlaa_ca', 'imlaa_exam', 'khot_ca', 'khot_exam', 'cumulative']
    search_fields = ['pupil__user__username', 'pupil__classe__name']
    list_filter = ['pupil__classe__name']
    list_display_links = ['pupil']
    list_editable = ['school_fees']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.pupil.classe
    get_classe.admin_order_field = 'pupil'
    get_classe.short_description = 'Class'

admin.site.register(FirstTerm, FirstTermAdmin)
