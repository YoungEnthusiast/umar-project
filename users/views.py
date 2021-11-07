import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.http import HttpResponseRedirect
from .forms import CustomRegisterForm, CustomRegisterFormStaff, CustomRegisterFormStudent, CustomRegisterFormStud, CustomRegisterFormAdmin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required#, permission_required
from django.contrib import messages
from .filters import StudentFilter, StaffFilter, StudentFilter2
from .models import Person
from management.models import Subject, Class, Session
from django.core.paginator import Paginator
#from django.core.mail import send_mail
from django.contrib.auth.models import User
#from django.template.loader import render_to_string
from result.models import First

@login_required
def createAdFirst(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful!")
            return redirect('index')
        else:
            messages.error(request, "Please review and correct form input fields")
            #return redirect('account')
    else:
        form = CustomRegisterForm()
    return render(request, 'users/account.html', {'form': form})

def createStaff(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful!")
            return redirect('index')
=======
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
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
        else:
            messages.error(request, "Please review and correct form input fields")
            #return redirect('account')
    else:
        form = CustomRegisterForm()
<<<<<<< HEAD
    return render(request, 'users/account_sta.html', {'form': form})

@login_required
def editProfileAdminFirst(request, **kwargs):
    if request.method == "POST":
        form = CustomRegisterFormAdmin(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('profile_admin_first')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = CustomRegisterFormAdmin(instance=request.user)
    return render(request, 'users/profile_admin.html', {'form': form})

@login_required
def editProfileStaffFirst(request, **kwargs):
    if request.method == "POST":
        form = CustomRegisterFormStaff(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('profile_staff_first')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = CustomRegisterFormStaff(instance=request.user)
    return render(request, 'users/profile_staff.html', {'form': form})

@login_required
def editProfileStudentFirst(request, **kwargs):
    if request.method == "POST":
        form = CustomRegisterFormStudent(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been modified successfully")
            return redirect('profile_student_first')
        else:
            messages.error(request, "Error: Please review form input fields below")
    else:
        form = CustomRegisterFormStudent(instance=request.user)
    return render(request, 'users/profile_student.html', {'form': form})
=======
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
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9

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
<<<<<<< HEAD
                'yustaoab@gmail.com',
=======
                'info@medcarehospitals.com.ng',
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
                [email],
                fail_silently=False,
                html_message = render_to_string('users/change_password_email.html', {'name': str(name)})
            )
            messages.success(request, "Your password has been changed")
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})
<<<<<<< HEAD

@login_required
def showStudentsFirst(request):
    context = {}
    filtered_students = StudentFilter(
        request.GET,
        queryset = Person.objects.filter(role="Student")
    )
    context['filtered_students'] = filtered_students
    paginated_filtered_students = Paginator(filtered_students.qs, 10)
    page_number = request.GET.get('page')
    students_page_obj = paginated_filtered_students.get_page(page_number)
    context['students_page_obj'] = students_page_obj
    total_students = filtered_students.qs.count()
    context['total_students'] = total_students
    return render(request, 'users/staff_students_first.html', context=context)

def showStudentsFirst2(request):
    context = {}
    filtered_students = StudentFilter2(
        request.GET,
        queryset = Person.objects.filter(role="Student")
    )
    context['filtered_students'] = filtered_students
    paginated_filtered_students = Paginator(filtered_students.qs, 10)
    page_number = request.GET.get('page')
    students_page_obj = paginated_filtered_students.get_page(page_number)
    context['students_page_obj'] = students_page_obj
    total_students = filtered_students.qs.count()
    context['total_students'] = total_students
    return render(request, 'users/admin_students_first.html', context=context)

def updateStudentsFirst(request, id):
    student = Person.objects.get(id=id)
    form = CustomRegisterFormStud(instance=student)
    if request.method=='POST':
        form = CustomRegisterFormStud(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "The student has been modified successfully")
            return redirect('admin_students_first')
    return render(request, 'users/student_update_first.html', {'form': form, 'student': student})

@login_required
def showStaffsFirst(request):
    context = {}
    filtered_staffs = StaffFilter(
        request.GET,
        queryset = Person.objects.filter(role="Staff")
    )
    context['filtered_staffs'] = filtered_staffs
    paginated_filtered_staffs = Paginator(filtered_staffs.qs, 10)
    page_number = request.GET.get('page')
    staffs_page_obj = paginated_filtered_staffs.get_page(page_number)
    context['staffs_page_obj'] = staffs_page_obj
    total_staffs = filtered_staffs.qs.count()
    context['total_staffs'] = total_staffs
    return render(request, 'users/admin_staff_first.html', context=context)

def updateStaffsFirst(request, id):
    staff = Person.objects.get(id=id)
    form = CustomRegisterFormStaff(instance=staff)
    if request.method=='POST':
        form = CustomRegisterFormStaff(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, "The staff has been modified successfully")
            return redirect('staffs_first')
    return render(request, 'users/staff_update_first.html', {'form': form, 'staff': staff})

@login_required
def deleteStaffFirst(request, id):
    staff = Person.objects.get(id=id)
    obj = get_object_or_404(Person, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('staffs_first')
    return render(request, 'users/staffs_confirm_delete.html', {'staff': staff})

@login_required
def deleteStudentFirst(request, id):
    student = Person.objects.get(id=id)
    obj = get_object_or_404(Person, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('admin_students_first')
    return render(request, 'users/students_confirm_delete.html', {'student': student})

@login_required
def showAdminBoardFirst(request):
    people = Person.objects.all().count()-1
    students = Person.objects.filter(role="Student").count()
    staff = Person.objects.filter(role="Staff").count()
    try:
        session = Session.objects.all()[0]
    except:
        session = None

    p_studs = First.objects.filter(session=session, value=1, school_fees=True).count()
    o_studs = First.objects.filter(session=session, value=1, school_fees=False).count()
    classes = Class.objects.all().count()
    subjects = Subject.objects.all().count()
    try:
        fir = First.objects.filter(value=1).order_by('-cumulative')[0]
    except:
        fir = " "
    try:
        sec = First.objects.filter(value=1).order_by('-cumulative')[1]
    except:
        sec = " "
    try:
        thi = First.objects.filter(value=1).order_by('-cumulative')[2]
    except:
        thi = " "

    context = {'session':session, 'students':students, 'people':people, 'staff':staff,
                'classes':classes, 'p_studs':p_studs, 'o_studs':o_studs, 'subjects':subjects,
                'fir':fir, 'sec':sec, 'thi':thi}
    return render(request, 'users/admin_board_first.html', context)

@login_required
def showStaffBoardFirst(request):
    subjects = Subject.objects.filter(teacher=request.user).count()
    try:
        sub1 = Subject.objects.filter(teacher=request.user)[0]
    except:
        sub1 = " "
    try:
        sub2 = Subject.objects.filter(teacher=request.user)[1]
    except:
        sub2 = " "
    try:
        sub3 = Subject.objects.filter(teacher=request.user)[2]
    except:
        sub3 = " "
    try:
        sub4 = Subject.objects.filter(teacher=request.user)[3]
    except:
        sub4 = " "
    try:
        sub5 = Subject.objects.filter(teacher=request.user)[4]
    except:
        sub5 = " "

    classes = Class.objects.filter(teacher=request.user).count()
    try:
        cla1 = Class.objects.filter(teacher=request.user)[0]
    except:
        cla1 = " "
    try:
        cla2 = Class.objects.filter(teacher=request.user)[1]
    except:
        cla2 = " "
    try:
        cla3 = Class.objects.filter(teacher=request.user)[2]
    except:
        cla3 = " "

    studs = Person.objects.filter(role="Student", classe__teacher=request.user).count()
    try:
        fir = First.objects.filter(student__classe__teacher=request.user, value=1).order_by('-cumulative')[0]
    except:
        fir = " "
    try:
        sec = First.objects.filter(student__classe__teacher=request.user, value=1).order_by('-cumulative')[1]
    except:
        sec = " "
    try:
        thi = First.objects.filter(student__classe__teacher=request.user, value=1).order_by('-cumulative')[2]
    except:
        thi = " "

    context = {'subjects':subjects, 'sub1':sub1, 'sub2':sub2, 'sub3':sub3,
                'classes':classes, 'cla1':cla1, 'cla2':cla2, 'cla3':cla3,
                'studs':studs, 'fir':fir, 'sec':sec, 'thi':thi}
    return render(request, 'users/staff_board_first.html', context)

@login_required
def showStudentBoardFirst(request):
    me = Person.objects.get(username=request.user.username)
    my_class = me.classe
    if my_class.teacher.gender == "Female":
        my_teacher = "Mrs " + my_class.teacher.first_name + " " + my_class.teacher.last_name
    else:
        my_teacher = "Mr " + my_class.teacher.first_name + " " + my_class.teacher.last_name
    studs = Person.objects.filter(classe=my_class).count()
    context = {'my_class':my_class, 'my_teacher':my_teacher, 'studs':studs}
    return render(request, 'users/student_board_first.html', context)

@login_required
def showStudent(request, pk, **kwargs):
    student = Person.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'users/student_detail.html', context)

@login_required
def showStudentAd(request, pk, **kwargs):
    student = Person.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'users/student_detail.html', context)

@login_required
def showStaff(request, pk, **kwargs):
    staff = Person.objects.get(id=pk)
    context = {'staff': staff}
    return render(request, 'users/staff_detail.html', context)

@login_required
def loginTo(request):
    if request.user.role == "Staff":
        return HttpResponseRedirect(reverse('staff_board_first'))
    elif request.user.role == "Student":
        return HttpResponseRedirect(reverse('student_board_first'))
    elif request.user.role == "A---n":
        return HttpResponseRedirect(reverse('admin_board_first'))
=======
>>>>>>> 221184f680b28065f815f25d581c3bf78f22eef9
