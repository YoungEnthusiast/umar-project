from django import forms
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstTermForm(forms.ModelForm):
    class Meta:
        model = FirstTerm
        fields = ['session', 'student', 'quran_ca', 'quran_exam', 'tajweed_ca',
        'tajweed_exam', 'nahw_ca', 'nahw_exam', 'sorf_ca', 'sorf_exam', 'uluum_ulquran_ca',
        'uluum_ulquran_exam', 'balaagah_ca', 'balaagah_exam', 'tawheed_ca', 'tawheed_exam',
        'farooid_ca', 'farooid_exam', 'fiqh_ca', 'fiqh_exam', 'taareekh_ca', 'taareekh_exam',
        'hadeeth_ca', 'hadeeth_exam', 'aruud_ca', 'aruud_exam', 'mantiqoh_ca', 'mantiqoh_exam',
        'tafseer_ca', 'tafseer_exam', 'mustolah_ulhadeeth_ca', 'mustolah_ulhadeeth_exam',
        'teacher_comment', 'head_comment']

class FirstTermFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstTermFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = FirstTerm
        fields = ['session', 'student', 'quran_ca', 'quran_exam', 'tajweed_ca',
        'tajweed_exam', 'nahw_ca', 'nahw_exam', 'sorf_ca', 'sorf_exam', 'uluum_ulquran_ca',
        'uluum_ulquran_exam', 'balaagah_ca', 'balaagah_exam', 'tawheed_ca', 'tawheed_exam',
        'farooid_ca', 'farooid_exam', 'fiqh_ca', 'fiqh_exam', 'taareekh_ca', 'taareekh_exam',
        'hadeeth_ca', 'hadeeth_exam', 'aruud_ca', 'aruud_exam', 'mantiqoh_ca', 'mantiqoh_exam',
        'tafseer_ca', 'tafseer_exam', 'mustolah_ulhadeeth_ca', 'mustolah_ulhadeeth_exam',
        'teacher_comment', 'head_comment']
