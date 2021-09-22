from django import forms
from .models import Session, Class, Subject
from django.core.exceptions import ValidationError

class SessionForm(forms.ModelForm):
    def clean_session(self):
       session = self.cleaned_data.get('session')
       if Session.objects.filter(session=session).exists():
           raise ValidationError("The session already exists")
       return session
    class Meta:
        model = Session
        fields = ['session', 'head', 'school', 'number', 'next', 'first_report']

class SessionFormUp(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session', 'head', 'school', 'number', 'next', 'first_report']

class ClassForm(forms.ModelForm):
    def clean_classe(self):
       classe = self.cleaned_data.get('classe')
       if Class.objects.filter(classe=classe).exists():
           raise ValidationError("The class already exists")
       return classe
    class Meta:
        model = Class
        fields = ['classe', 'teacher', 'signature']

class ClassFormUp(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['classe', 'teacher', 'signature']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['serial', 'classe', 'subject', 'teacher']
