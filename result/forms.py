from django import forms
from .models import First

class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ['session', 'subject', 'ca1', 'ca2', 'exam']


class FirstFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['subject'].required = False
            self.fields['subject'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'subject', 'ca1', 'ca2', 'exam']

class FirstFormBeha(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    def __init__(self, *args, **kwargs):
        super(FirstFormBeha, self).__init__(*args, **kwargs)
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

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'number_present', 'concentration', 'responsiveness', 'comprehension',
        'interest', 'homework', 'reading', 'writing', 'spoken', 'innovative']

class FirstFormPay(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstFormPay, self).__init__(*args, **kwargs)
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

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'school_fees']
