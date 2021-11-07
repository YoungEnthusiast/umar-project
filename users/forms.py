from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
<<<<<<< HEAD
#from django.contrib.auth.models import User
=======
from django.contrib.auth.models import User
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
from .models import Person
from django.core.exceptions import ValidationError
import datetime
from django.forms.widgets import NumberInput

class CustomRegisterForm(UserCreationForm):
<<<<<<< HEAD
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),

    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    role = forms.ChoiceField(label='User Type', choices=ROLE_CHOICES)
    #subject = forms.CharField(max_length=255)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #address = forms.CharField(max_length=200, required=False)
=======
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
<<<<<<< HEAD
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if Person.objects.filter(username=username).exists():
           raise ValidationError("A user with the supplied username already exists")
       return username

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'role', 'subject', 'username', 'password1', 'password2', 'classe', 'phone_number', 'gender', 'address', 'dob',  'photograph']
=======

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if User.objects.filter(username=username).exists():
           raise ValidationError("A user with the supplied username already exists")
       return username

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name'}
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Admission No (Username)'
<<<<<<< HEAD
        self.fields['username'].help_text = "For staff, choose a username for logging in in subsequent times"
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other Personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        self.fields['role'].help_text = "Select Staff if you are a teacher"
###
class CustomRegisterFormAdmin(UserChangeForm):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('A---n', 'A---n')
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email
    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'gender', 'address', 'dob',  'photograph']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Username'
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"

class CustomRegisterFormStaff(UserChangeForm):
=======
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"

class UserEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

class PersonEditForm(forms.ModelForm):
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
<<<<<<< HEAD
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('A---n', 'A---n')
=======
        ('Pupil', 'Pupil'),
        ('Student', 'Student'),
        ('Staff', 'Staff'),
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
<<<<<<< HEAD
    address = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email
=======
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)

>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
<<<<<<< HEAD
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'gender', 'address', 'dob', 'subject', 'photograph']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Username'
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"

class CustomRegisterFormStudent(UserChangeForm):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('A---n', 'A---n')
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    def __init__(self, *args, **kwargs):
        super(CustomRegisterFormStudent, self).__init__(*args, **kwargs)
=======
        fields = ['phone_number', 'gender', 'address', 'dob', 'classe', 'role', 'photograph']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        self.fields['role'].label = "Role"

class UserEditForm2(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

    def __init__(self, *args, **kwargs):
        super(UserEditForm2, self).__init__(*args, **kwargs)
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs['disabled'] = 'disabled'
            self.fields['first_name'].required = False
            self.fields['first_name'].widget.attrs['disabled'] = 'disabled'
            self.fields['last_name'].required = False
            self.fields['last_name'].widget.attrs['disabled'] = 'disabled'
<<<<<<< HEAD
            self.fields['classe'].required = False
            self.fields['classe'].widget.attrs['disabled'] = 'disabled'
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['username'].label = 'Admission No'
            self.fields['email'].help_text = "This field must be a valid email address"
            self.fields['phone_number'].label = "Phone Number"
            self.fields['dob'].label = "Date of Birth"

    def clean_username(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.username
        else:
            return self.cleaned_data.get('username', None)

    def clean_first_name(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.first_name
        else:
            return self.cleaned_data.get('first_name', None)

    def clean_last_name(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.last_name
        else:
            return self.cleaned_data.get('last_name', None)

    def clean_classe(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.classe
        else:
            return self.cleaned_data.get('classe', None)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'username', 'classe', 'phone_number', 'gender', 'address', 'dob',  'photograph']

class CustomRegisterFormStud(UserChangeForm):
=======

class PersonEditForm2(forms.ModelForm):
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
<<<<<<< HEAD
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('A---n', 'A---n')
=======
        ('Pupil', 'Pupil'),
        ('Student', 'Student'),
        ('Staff', 'Staff'),
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
<<<<<<< HEAD
    address = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email
=======
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

<<<<<<< HEAD
    # def __init__(self, *args, **kwargs):
    #     super(CustomRegisterFormStudent, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.id:
    #         self.fields['username'].required = False
    #         self.fields['username'].widget.attrs['disabled'] = 'disabled'
    #         self.fields['first_name'].required = False
    #         self.fields['first_name'].widget.attrs['disabled'] = 'disabled'
    #         self.fields['last_name'].required = False
    #         self.fields['last_name'].widget.attrs['disabled'] = 'disabled'
    #         self.fields['classe'].required = False
    #         self.fields['classe'].widget.attrs['disabled'] = 'disabled'
    #         self.fields['first_name'].label = 'First Name'
    #         self.fields['last_name'].label = 'Last Name'
    #         self.fields['username'].label = 'Admission No'
    #         self.fields['email'].help_text = "This field must be a valid email address"
    #         self.fields['phone_number'].label = "Phone Number"
    #         self.fields['dob'].label = "Date of Birth"
    #
    # def clean_username(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.username
    #     else:
    #         return self.cleaned_data.get('username', None)
    #
    # def clean_first_name(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.first_name
    #     else:
    #         return self.cleaned_data.get('first_name', None)
    #
    # def clean_last_name(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.last_name
    #     else:
    #         return self.cleaned_data.get('last_name', None)
    #
    # def clean_classe(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.classe
    #     else:
    #         return self.cleaned_data.get('classe', None)

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'username', 'classe', 'phone_number', 'gender', 'address', 'dob',  'photograph']
=======
    class Meta:
        model = Person
        fields = ['phone_number', 'gender', 'address', 'dob', 'classe', 'role', 'photograph']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        self.fields['role'].label = "Role"

    def __init__(self, *args, **kwargs):
        super(PersonEditForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['classe'].required = False
            self.fields['classe'].widget.attrs['disabled'] = 'disabled'
            self.fields['role'].required = False
            self.fields['role'].widget.attrs['disabled'] = 'disabled'
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
