from django import forms
from .models import FirstTerm#, SecondTerm, ThirdTerm

class FirstTermForm(forms.ModelForm):
    class Meta:
        model = FirstTerm
        fields = ['session', 'pupil', 'quran_ca', 'quran_exam', 'tajweed_ca', 'tajweed_exam',
        'mutoolaah_ca', 'mutoolaah_exam', 'arabiyyah_ca', 'arabiyyah_exam', 'nahw_ca',
        'nahw_exam', 'tawheed_ca', 'tawheed_exam', 'fiqh_ca', 'fiqh_exam', 'seeroh_ca',
        'seeroh_exam', 'hadeeth_ca', 'hadeeth_exam', 'imlaa_ca', 'imlaa_exam', 'khot_ca',
        'khot_exam', 'teacher_comment', 'head_comment']

class FirstTermFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstTermFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['pupil'].required = False
            self.fields['pupil'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_pupil(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.pupil
        else:
            return self.cleaned_data.get('pupil', None)

    class Meta:
        model = FirstTerm
        fields = ['session', 'pupil', 'quran_ca', 'quran_exam', 'tajweed_ca', 'tajweed_exam',
        'mutoolaah_ca', 'mutoolaah_exam', 'arabiyyah_ca', 'arabiyyah_exam', 'nahw_ca',
        'nahw_exam', 'tawheed_ca', 'tawheed_exam', 'fiqh_ca', 'fiqh_exam', 'seeroh_ca',
        'seeroh_exam', 'hadeeth_ca', 'hadeeth_exam', 'imlaa_ca', 'imlaa_exam', 'khot_ca',
        'khot_exam', 'teacher_comment', 'head_comment']
