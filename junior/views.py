from django.shortcuts import render, redirect
from .models import FirstTerm#, SecondTerm, ThirdTerm
from .forms import FirstTermForm, FirstTermFormUp#, SecondTermForm, SecondTermFormUp, ThirdTermForm, ThirdTermFormUp
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import FirstFilter#, SecondFilter, ThirdFilter
from django.contrib.auth.decorators import login_required#, permission_required
from django.core.mail import send_mail
#from django.template.loader import render_to_string

@login_required
def showFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = FirstTerm.objects.all()
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'junior/first_list.html', context=context)

@login_required
def showFirstsUser(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = FirstTerm.objects.filter(student__user=request.user, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'junior/first_list_user.html', context=context)

@login_required
def updateFirsts(request, id):
    first = FirstTerm.objects.get(id=id)
    form = FirstTermFormUp(instance=first)
    if request.method=='POST':
        form = FirstTermFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            teacher_comment = form.cleaned_data.get('teacher_comment')
            head_comment = form.cleaned_data.get('head_comment')
            student_first_name = student.user.first_name
            student_last_name = student.user.last_name
            student_email = student.user.email
            reg = FirstTerm.objects.get(student=student)
            quran_tot = reg.quran_ca + reg.quran_exam
            tajweed_tot = reg.tajweed_ca + reg.tajweed_exam
            mutoolaah_tot = reg.mutoolaah_ca + reg.mutoolaah_exam
            arabiyyah_tot = reg.arabiyyah_ca + reg.arabiyyah_exam
            nahw_tot = reg.nahw_ca + reg.nahw_exam
            tawheed_tot = reg.tawheed_ca + reg.tawheed_exam
            fiqh_tot = reg.fiqh_ca + reg.fiqh_exam
            seeroh_tot = reg.seeroh_ca + reg.seeroh_exam
            hadeeth_tot = reg.hadeeth_ca + reg.hadeeth_exam
            nusuus_tot = reg.nusuus_ca + reg.nusuus_exam
            tabeer_tot = reg.tabeer_ca + reg.tabeer_exam
            duruusu_tot = reg.duruusu_ca + reg.duruusu_exam
            hadeethulhifz_tot = reg.hadeethulhifz_ca + reg.hadeethulhifz_exam

            cumulative = (quran_tot + tajweed_tot + mutoolaah_tot + arabiyyah_tot
            + nahw_tot + tawheed_tot + fiqh_tot + seeroh_tot + hadeeth_tot + nusuus_tot
            + tabeer_tot + duruusu_tot + hadeethulhifz_tot
            )
            reg.quran_tot = quran_tot
            reg.tajweed_tot = tajweed_tot
            reg.mutoolaah_tot = mutoolaah_tot
            reg.arabiyyah_tot = arabiyyah_tot
            reg.nahw_tot = nahw_tot
            reg.tawheed_tot = tawheed_tot
            reg.fiqh_tot = fiqh_tot
            reg.seeroh_tot = seeroh_tot
            reg.hadeeth_tot = hadeeth_tot
            reg.nusuus_tot = nusuus_tot
            reg.tabeer_tot = tabeer_tot
            reg.duruusu_tot = duruusu_tot
            reg.hadeethulhifz_tot = hadeethulhifz_tot
            reg.cumulative = cumulative
            reg.teacher_comment = teacher_comment
            reg.head_comment = head_comment
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
                'yustaoab@gmail.com',
                [student_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('junior_firsts')
    return render(request, 'junior/first_form_update.html', {'form': form, 'first': first})

@login_required
def addFirst(request, **kwargs):
    form = FirstTermForm()
    if request.method == 'POST':
        form = FirstTermForm(request.POST or None)
        if form.is_valid():
            form.save()
            teacher = request.user
            teacher_name = teacher.last_name
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            teacher_comment = form.cleaned_data.get('teacher_comment')
            head_comment = form.cleaned_data.get('head_comment')
            student_first_name = student.user.first_name
            student_last_name = student.user.last_name
            student_email = student.user.email
            reg = FirstTerm.objects.get(student=student)
            quran_tot = reg.quran_ca + reg.quran_exam
            tajweed_tot = reg.tajweed_ca + reg.tajweed_exam
            mutoolaah_tot = reg.mutoolaah_ca + reg.mutoolaah_exam
            arabiyyah_tot = reg.arabiyyah_ca + reg.arabiyyah_exam
            nahw_tot = reg.nahw_ca + reg.nahw_exam
            tawheed_tot = reg.tawheed_ca + reg.tawheed_exam
            fiqh_tot = reg.fiqh_ca + reg.fiqh_exam
            seeroh_tot = reg.seeroh_ca + reg.seeroh_exam
            hadeeth_tot = reg.hadeeth_ca + reg.hadeeth_exam
            nusuus_tot = reg.nusuus_ca + reg.nusuus_exam
            tabeer_tot = reg.tabeer_ca + reg.tabeer_exam
            duruusu_tot = reg.duruusu_ca + reg.duruusu_exam
            hadeethulhifz_tot = reg.hadeethulhifz_ca + reg.hadeethulhifz_exam

            cumulative = (quran_tot + tajweed_tot + mutoolaah_tot + arabiyyah_tot
            + nahw_tot + tawheed_tot + fiqh_tot + seeroh_tot + hadeeth_tot + nusuus_tot
            + tabeer_tot + duruusu_tot + hadeethulhifz_tot
            )
            reg.quran_tot = quran_tot
            reg.tajweed_tot = tajweed_tot
            reg.mutoolaah_tot = mutoolaah_tot
            reg.arabiyyah_tot = arabiyyah_tot
            reg.nahw_tot = nahw_tot
            reg.tawheed_tot = tawheed_tot
            reg.fiqh_tot = fiqh_tot
            reg.seeroh_tot = seeroh_tot
            reg.hadeeth_tot = hadeeth_tot
            reg.nusuus_tot = nusuus_tot
            reg.tabeer_tot = tabeer_tot
            reg.duruusu_tot = duruusu_tot
            reg.hadeethulhifz_tot = hadeethulhifz_tot
            reg.cumulative = cumulative
            reg.teacher_comment = teacher_comment
            reg.head_comment = head_comment
            reg.save()
            send_mail(
                '[' + str(session) + '] SCORES UPDATE',
                'New Scores have been recorded. Current Total: ' + str(cumulative) + "Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
                'yustaoab@gmail.com',
                [student_email],
                fail_silently=False,
                #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            )
            messages.success(request, str(student_first_name) + "'s score has been added successfully")
            return redirect('junior_first')
        else:
            messages.error(request, "Please review form input fields below")
            #return redirect('junior_first')
    return render(request, 'junior/first_form.html', {'form': form})

@login_required
def showFirst(request, **kwargs):
    first = FirstTerm.objects.filter(id=kwargs['pk'])
    response_first = []
    for each in first:
        class_students_count = FirstTerm.objects.filter(student__classe=each.student.classe).count()
        class_students = FirstTerm.objects.filter(student__classe=each.student.classe)

        position = []
        pos = 0
        for student in class_students:
            position.append(student.cumulative)
            position.sort(reverse=True)

        for i in range(len(position)):
            if position[i] == each.cumulative:
                if i in range (10, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (11, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (12, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (0, len(position), 10):
                    pos = str(i + 1) + "st"
                elif i in range (1, len(position), 10):
                    pos = str(i + 1) + "nd"
                elif i in range (2, len(position), 10):
                    pos = str(i + 1) + "rd"
                else:
                    pos = str(i + 1) + "th"

        response_first.append(each)
    return render(request, 'junior/first_report.html', {'first': response_first,
        'class_students_count': class_students_count, 'pos': pos})

@login_required
def showFirstUser(request, **kwargs):
    first = FirstTerm.objects.filter(id=kwargs['pk'])
    response_first = []
    for each in first:
        class_students_count = FirstTerm.objects.filter(student__classe=each.student.classe).count()
        class_students = FirstTerm.objects.filter(student__classe=each.student.classe)

        position = []
        pos = 0
        for student in class_students:
            position.append(student.cumulative)
            position.sort(reverse=True)

        for i in range(len(position)):
            if position[i] == each.cumulative:
                if i in range (10, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (11, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (12, len(position), 100):
                    pos = str(i + 1) + "th"
                elif i in range (0, len(position), 10):
                    pos = str(i + 1) + "st"
                elif i in range (1, len(position), 10):
                    pos = str(i + 1) + "nd"
                elif i in range (2, len(position), 10):
                    pos = str(i + 1) + "rd"
                else:
                    pos = str(i + 1) + "th"

        response_first.append(each)
    return render(request, 'junior/first_report_user.html', {'first': response_first,
        'class_students_count': class_students_count, 'pos': pos})
