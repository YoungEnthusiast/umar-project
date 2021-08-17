import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm, UserEditForm, PersonEditForm, UserEditForm2, PersonEditForm2
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required#, permission_required
from .models import Person
from records.models import Pupil, Student
from staff.models import Teacher
#from django.core.mail import send_mail
from django.contrib.auth.models import User
#from django.template.loader import render_to_string

def create(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  ('Initial registration was successful! Please sign in below and then complete your registration.'))
            return redirect('edit_profile0')

            # name = form.cleaned_data.get('first_name')
            # email = form.cleaned_data.get('email')
            #
            # return redirect('edit_profile')
        else:
            messages.error(request, "Please review and correct form input fields")
            #return redirect('account')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/account.html', {'form': form})

@login_required
def editProfile0(request, **kwargs):
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        person_form = PersonEditForm(request.POST, request.FILES, instance=request.user.person)
        if form.is_valid() and person_form.is_valid():
            form.save()
            person_form.save()
            #profile = UserProfile.objects.create(user=request.user)
            new_person = Person.objects.get_or_create(user=request.user)
            new_person.save()
            if new_person.role == "Pupil" and new_person.classe == None:
                messages.error(request, "Error: Please Choose a class to save pupil")
            elif new_person.role == "Student" and new_person.classe == None:
                messages.error(request, "Error: Please Choose a class to save student")
            elif new_person.role == "Pupil" and new_person.classe != None:
                new_pupil = Pupil()
                new_pupil.user = new_person.user
                new_pupil.first_name = new_person.user.first_name
                new_pupil.last_name = new_person.user.last_name
                new_pupil.phone_number = new_person.phone_number
                new_pupil.gender = new_person.gender
                new_pupil.address = new_person.address
                new_pupil.dob = new_person.dob
                new_pupil.photograph = new_person.photograph
                new_pupil.classe = new_person.classe
                new_pupil.created = new_person.created
                new_pupil.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('index')
            elif new_person.role == "Student" and new_person.classe != None:
                new_student = Student()
                new_student.user = new_person.user
                new_student.first_name = new_person.user.first_name
                new_student.last_name = new_person.user.last_name
                new_student.phone_number = new_person.phone_number
                new_student.gender = new_person.gender
                new_student.address = new_person.address
                new_student.dob = new_person.dob
                new_student.photograph = new_person.photograph
                new_student.classe = new_person.classe
                new_student.created = new_person.created
                new_student.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('index')
            elif new_person.role == "Staff":
                new_teacher = Teacher()
                new_teacher.user = new_person.user
                new_teacher.first_name = new_person.user.first_name
                new_teacher.last_name = new_person.user.last_name
                new_teacher.phone_number = new_person.phone_number
                new_teacher.gender = new_person.gender
                new_teacher.address = new_person.address
                new_teacher.dob = new_person.dob
                new_teacher.classe = new_person.classe
                new_teacher.created = new_person.created

                new_teacher.save()
                messages.success(request, "The Profile has been modified successfully")
                return redirect('index')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = UserEditForm(instance=request.user)
        person_form = PersonEditForm(instance=request.user.person)
    return render(request, 'users/edit_profile.html', {'form': form, 'person_form': person_form})

@login_required
def editProfile(request, **kwargs):
    if request.method == "POST":
        form = UserEditForm2(request.POST, request.FILES, instance=request.user.person)
        person_form = PersonEditForm2(request.POST, request.FILES, instance=request.user.person)
        #if person_form.is_valid():
        if form.is_valid() and person_form.is_valid():
            form.save()
            person_form.save()
            new_person = Person.objects.get(user=request.user)
            new_person.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('edit_profile')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = UserEditForm2(instance=request.user)
        person_form = PersonEditForm2(instance=request.user.person)
    return render(request, 'users/edit_profile.html', {'form': form, 'person_form': person_form})

@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            user = request.user
            name = user.first_name
            email = user.email
            send_mail(
                'Password Changed!',
                'Dear ' + str(name) + ', your password has just been changed. If this activity was not carried out by you, please reply to this email',
                'info@medcarehospitals.com.ng',
                [email],
                fail_silently=False,
                html_message = render_to_string('users/change_password_email.html', {'name': str(name)})
            )
            messages.success(request, "Your password has been changed")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})
