from django.shortcuts import render, redirect, get_object_or_404
from .models import First
from users.models import Person
from .forms import FirstForm, FirstFormUp, FirstFormBeha, FirstFormPay
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import FirstFilter, FirstFilter2, FirstFilterPay
from django.contrib.auth.decorators import login_required#, permission_required
from django.core.mail import send_mail
from django.db.models import Sum
#from django.template.loader import render_to_string

@login_required
def showFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(subject__teacher=request.user)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list.html', context=context)

@login_required
def showAdminFirsts(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.all()
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list.html', context=context)

@login_required
def showFirsts2(request, ):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list2.html', context=context)

@login_required
def showAdminFirsts2(request, ):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list2.html', context=context)

@login_required
def showFirsts3(request):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(student__classe__teacher=request.user, value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list3.html', context=context)

@login_required
def showAdminFirsts3(request):
    context = {}
    filtered_firsts = FirstFilter2(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/admin_first_list3.html', context=context)

@login_required
def showFirstsUser(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(student=request.user, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list_user.html', context=context)

@login_required
def showFirsts3User(request):
    context = {}
    filtered_firsts = FirstFilter(
        request.GET,
        queryset = First.objects.filter(session__first_report=True, student=request.user, value=1, school_fees=True)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_list3_user.html', context=context)

@login_required
def updateFirst(request, id):
    first = First.objects.get(id=id)
    form = FirstFormUp(instance=first)
    if request.method=='POST':
        form = FirstFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            reg = First.objects.get(session=session, student=student, subject=subject)
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
                reg.delete()
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                old_total = reg.total
                new_total = reg.ca1 + reg.ca2 + reg.exam
                reg.total = new_total
                reg.save()
                reg1 = First.objects.get(session=session, student=student, subject=subject)
                reg1.subject_total = reg1.subject_total - old_total
                reg1.save()
                reg2 = First.objects.get(session=session, student=student, subject=subject)
                reg2.subject_total = reg2.subject_total + new_total
                reg2.save()
                reg3 = First.objects.get(session=session, student=student, subject=subject)
                reg4 = First.objects.filter(session=session, subject=subject)
                n = reg4.count()
                d = round((reg3.subject_total/n),2)
                subject_position = []
                subject_pos = 0

                for each in reg4:
                    each.subject_total = reg3.subject_total
                    each.subject_avg = d
                    each.grade = reg3.grade()
                    subject_position.append(each.total)
                    subject_position.sort(reverse=True)
                    each.save()
                for each in reg4:
                    for i in range(len(subject_position)):
                        if subject_position[i] == each.total:
                            if i in range (10, len(subject_position), 100):
                                subject_pos = str(i + 1) + "th"
                                each.subject_pos = subject_pos
                                each.save()
                            elif i in range (11, len(subject_position), 100):
                                subject_pos = str(i + 1) + "th"
                                each.subject_pos = subject_pos
                                each.save()
                            elif i in range (12, len(subject_position), 100):
                                subject_pos = str(i + 1) + "th"
                                each.subject_pos = subject_pos
                                each.save()
                            elif i in range (0, len(subject_position), 10):
                                subject_pos = str(i + 1) + "st"
                                each.subject_pos = subject_pos
                                each.save()
                            elif i in range (1, len(subject_position), 10):
                                subject_pos = str(i + 1) + "nd"
                                each.subject_pos = subject_pos
                                each.save()
                            elif i in range (2, len(subject_position), 10):
                                subject_pos = str(i + 1) + "rd"
                                each.subject_pos = subject_pos
                                each.save()
                            else:
                                subject_pos = str(i + 1) + "th"
                                each.subject_pos = subject_pos
                                each.save()
                reg6 = First.objects.filter(session=session, student=student)
                m = reg6.count()
                all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
                cum_perc = round((all_total/m),2)
                for each in reg6:
                    each.cumulative = all_total
                    each.cum_perc = cum_perc
                    each.static_class = str(each.student.classe)
                    each.save()

            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('firsts')
    return render(request, 'result/first_update.html', {'form': form, 'first': first})

@login_required
def updateAdminFirst(request, id):
    first = First.objects.get(id=id)
    form = FirstFormUp(instance=first)
    if request.method=='POST':
        form = FirstFormUp(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            subject = form.cleaned_data.get('subject')
            reg = First.objects.get(session=session, student=student, subject=subject)
            reg.student = student
            teacher = request.user
            teacher_name = teacher.last_name
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            old_total = reg.total
            new_total = reg.ca1 + reg.ca2 + reg.exam
            reg.total = new_total
            reg.save()
            reg1 = First.objects.get(session=session, student=student, subject=subject)
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
            reg2 = First.objects.get(session=session, student=student, subject=subject)
            reg2.subject_total = reg2.subject_total + new_total
            reg2.save()
            reg3 = First.objects.get(session=session, student=student, subject=subject)
            reg4 = First.objects.filter(session=session, subject=subject)
            n = reg4.count()
            d = round((reg3.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg3.subject_total
                each.subject_avg = d
                each.grade = reg3.grade()
                subject_position.append(each.total)
                subject_position.sort(reverse=True)
                each.save()
            for each in reg4:
                for i in range(len(subject_position)):
                    if subject_position[i] == each.total:
                        if i in range (10, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (11, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (12, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (0, len(subject_position), 10):
                            subject_pos = str(i + 1) + "st"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (1, len(subject_position), 10):
                            subject_pos = str(i + 1) + "nd"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (2, len(subject_position), 10):
                            subject_pos = str(i + 1) + "rd"
                            each.subject_pos = subject_pos
                            each.save()
                        else:
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()

        # send_mail(
        #     '[' + str(session) + '] SCORES UPDATE',
        #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
        #     'yustaoab@gmail.com',
        #     [student_email],
        #     fail_silently=False,
        #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
        # )
            messages.success(request, str(student_first_name) + "'s score has been modified successfully")
            return redirect('admin_firsts')
    return render(request, 'result/admin_first_update.html', {'form': form, 'first': first})

@login_required
def updateFirstBeha(request, id):
    first = First.objects.get(id=id)
    form = FirstFormBeha(instance=first)
    if request.method=='POST':
        form = FirstFormBeha(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            if reg.student.classe.teacher != request.user:
                messages.error(request, "Only the class teacher of " + str(reg.student.classe) + " fill skills/attitudes for a student in the class.")
                reg.delete()
            else:
                reg.student = student
                teacher = request.user
                teacher_name = teacher.last_name
                student_first_name = student.first_name
                student_last_name = student.last_name
                student_email = student.email
                reg.save()
                reg1 = First.objects.filter(session=session, student=student)
                for each in reg1:
                    each.number_present = reg.number_present
                    each.concentration = reg.concentration
                    each.responsiveness = reg.responsiveness
                    each.comprehension = reg.comprehension
                    each.interest = reg.interest
                    each.homework = reg.homework
                    each.reading = reg.reading
                    each.writing = reg.writing
                    each.spoken = reg.spoken
                    each.innovative = reg.innovative
                    each.static_number = str(reg.session.number)
                    each.static_next = str(reg.session.next)
                    each.save()
            # send_mail(
            #     '[' + str(session) + '] SCORES UPDATE',
            #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
            #     'yustaoab@gmail.com',
            #     [student_email],
            #     fail_silently=False,
            #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
            # )
            messages.success(request, str(student_first_name) + "'s attitude to study and scholastic skills have been recorded successfully")
            return redirect('firsts2')
    return render(request, 'result/first_update_beha.html', {'form': form, 'first': first})

@login_required
def updateAdminFirstBeha(request, id):
    first = First.objects.get(id=id)
    form = FirstFormBeha(instance=first)
    if request.method=='POST':
        form = FirstFormBeha(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            reg.student = student
            teacher = request.user
            teacher_name = teacher.last_name
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            reg.save()
            reg1 = First.objects.filter(session=session, student=student)
            for each in reg1:
                each.number_present = reg.number_present
                each.concentration = reg.concentration
                each.responsiveness = reg.responsiveness
                each.comprehension = reg.comprehension
                each.interest = reg.interest
                each.homework = reg.homework
                each.reading = reg.reading
                each.writing = reg.writing
                each.spoken = reg.spoken
                each.innovative = reg.innovative
                each.static_number = str(reg.session.number)
                each.static_next = str(reg.session.next)
                each.save()
        # send_mail(
        #     '[' + str(session) + '] SCORES UPDATE',
        #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(student) + "student's Name: " + str(student_first_name) + str(student_last_name),
        #     'yustaoab@gmail.com',
        #     [student_email],
        #     fail_silently=False,
        #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
        # )
            messages.success(request, str(student_first_name) + "'s attitude to study and scholastic skills have been recorded successfully")
            return redirect('admin_firsts2')
    return render(request, 'result/admin_first_update_beha.html', {'form': form, 'first': first})

@login_required
def addFirst(request, id):
    stud = Person.objects.get(id=id)
    teacher = request.user
    teacher_name = teacher.last_name
    student_first_name = stud.first_name
    student_last_name = stud.last_name
    student_email = stud.email
    form = FirstForm()
    if request.method=='POST':
        form = FirstForm(request.POST or None)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            subject = form.cleaned_data.get('subject')
            reg = First.objects.filter(session=session, subject=subject)[0]
            if reg.subject.teacher != request.user:
                messages.error(request, "You cannot record a score for " + str(subject) + " because you were not assigned as the subject's teacher")
                reg.delete()
            else:
                try:
                    reg2 = First.objects.filter(session=session, student=stud, subject=subject)[0]
                    messages.error(request, student_first_name + " already exists in the score sheet for " + str(subject) +". To modify, click Scores by the left panel")
                    reg.delete()
                except:
                    reg.student = stud
                    teacher = request.user
                    teacher_name = teacher.last_name
                    student_first_name = stud.first_name
                    student_last_name = stud.last_name
                    student_email = stud.email
                    total = reg.ca1 + reg.ca2 + reg.exam
                    reg.total = total
                    reg.save()
                    try:
                        reg7 = First.objects.get(session=session, student=stud)
                        reg7.value = 1
                        reg7.save()
                    except:
                        pass
                    reg4 = First.objects.filter(session=session, subject=subject)
                    n = reg4.count()
                    try:
                        reg3 = First.objects.filter(session=session, subject=subject)[1]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = First.objects.filter(session=session, subject=subject)[1]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        subject_pos = 0
                    except:
                        reg3 = First.objects.filter(session=session, subject=subject)[0]
                        reg3.subject_total = reg3.subject_total + total
                        reg3.save()
                        reg5 = First.objects.filter(session=session, subject=subject)[0]
                        d = round((reg5.subject_total/n),2)
                        subject_position = []
                        subject_pos = 0
                    for each in reg4:
                        each.subject_total = reg5.subject_total
                        each.subject_avg = d
                        each.grade = reg5.grade()
                        subject_position.append(each.total)
                        subject_position.sort(reverse=True)
                        each.save()
                    for each in reg4:
                        for i in range(len(subject_position)):
                            if subject_position[i] == each.total:
                                if i in range (10, len(subject_position), 100):
                                    subject_pos = str(i + 1) + "th"
                                    each.subject_pos = subject_pos
                                    each.save()
                                elif i in range (11, len(subject_position), 100):
                                    subject_pos = str(i + 1) + "th"
                                    each.subject_pos = subject_pos
                                    each.save()
                                elif i in range (12, len(subject_position), 100):
                                    subject_pos = str(i + 1) + "th"
                                    each.subject_pos = subject_pos
                                    each.save()
                                elif i in range (0, len(subject_position), 10):
                                    subject_pos = str(i + 1) + "st"
                                    each.subject_pos = subject_pos
                                    each.save()
                                elif i in range (1, len(subject_position), 10):
                                    subject_pos = str(i + 1) + "nd"
                                    each.subject_pos = subject_pos
                                    each.save()
                                elif i in range (2, len(subject_position), 10):
                                    subject_pos = str(i + 1) + "rd"
                                    each.subject_pos = subject_pos
                                    each.save()
                                else:
                                    subject_pos = str(i + 1) + "th"
                                    each.subject_pos = subject_pos
                                    each.save()
                    reg6 = First.objects.filter(session=session, student=stud)
                    m = reg6.count()
                    all_total = First.objects.filter(session=session, student=stud).aggregate(Sum('total'))['total__sum']
                    cum_perc = round((all_total/m),2)
                    for each in reg6:
                        each.cumulative = all_total
                        each.cum_perc = cum_perc
                        each.static_class = str(each.student.classe)
                        each.save()
                    try:
                        reg8 = First.objects.get(session=session, student=stud, value=1)
                        if reg8.school_fees == True:
                            reg9 = First.objects.filter(session=session, student=stud)[0]
                            reg9.school_fees = True
                            reg9.save()
                    except:
                        pass


                    # send_mail(
                    #     '[' + str(session) + '] SCORES UPDATE',
                    #     "New Scores have been recorded. Teacher's Name: " + str(teacher_name) + "student: " + str(stud) + "student's Name: " + str(student_first_name) + str(student_last_name),
                    #     'yustaoab@gmail.com',
                    #     [student_email],
                    #     fail_silently=False,
                    #     #html_message = render_to_string('treatment/doc_lab_email.html', {'appointment_Id': str(appointment_Id), 'patient_id': str(patient_id), 'doctor_name': str(doctor_name), 'lab_technician_name': str(lab_technician_name), 'appointment_Id': str(appointment_Id)})
                    # )
                    messages.success(request, str(student_first_name) + "'s score has been added successfully")
                    return redirect('staff_students_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'result/first.html', {'form': form, 'student_first_name': student_first_name, 'student_last_name': student_last_name,})

@login_required
def showReportUser(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        class_students_count = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject).count()
        class_students = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject)
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_user.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'class_students_count':class_students_count,
    'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportCt(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        class_students_count = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject).count()
        class_students = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject)
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_ct.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'class_students_count':class_students_count,
    'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def showReportAdmin(request, pk, **kwargs):
    first = First.objects.get(id=pk)
    student = first.student
    session = first.session
    firsts = First.objects.all()
    firsts_student = First.objects.filter(session=session, student=student).order_by('subject__serial')
    obtainable = First.objects.filter(session=session, student=student).count()
    obtainable = 100 * obtainable
    grade_general = first.grade_general
    teacher_comment = first.teacher_comment
    head_comment = first.head_comment
    response_first = []
    response_first_student = []
    for each in firsts:
        class_students_count = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject).count()
        class_students = First.objects.filter(session=session, student__classe=each.student.classe, subject=each.subject)
        response_first.append(each)
    for each in firsts_student:
        response_first_student.append(each)
    return render(request, 'result/first_report_admin.html', {'firsts':response_first,
    'firsts_student':response_first_student, 'class_students_count':class_students_count,
    'first': first, 'obtainable':obtainable, 'grade_general':grade_general,
    'teacher_comment':teacher_comment, 'head_comment':head_comment})

@login_required
def deleteFirst(request, id):
    first = First.objects.get(id=id)
    obj = get_object_or_404(First, id=id)
    session = first.session
    student = first.student
    subject = first.subject
    reg = First.objects.get(session=session, student=student, subject=subject)
    old_total = reg.total
    value = reg.value
    if request.method =="POST":
        obj.delete()
        try:
            reg1 = First.objects.filter(session=session, subject=subject)[0]
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
        except:
            pass
        try:
            reg2 = First.objects.filter(session=session, subject=subject)[0]
            reg4 = First.objects.filter(session=session, subject=subject)
            n = reg4.count()
            d = round((reg2.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg2.subject_total
                each.subject_avg = d
                each.grade = reg2.grade()
                each.save()
            for each in reg4:
                for i in range(len(subject_position)):
                    if subject_position[i] == each.total:
                        if i in range (10, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (11, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (12, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (0, len(subject_position), 10):
                            subject_pos = str(i + 1) + "st"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (1, len(subject_position), 10):
                            subject_pos = str(i + 1) + "nd"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (2, len(subject_position), 10):
                            subject_pos = str(i + 1) + "rd"
                            each.subject_pos = subject_pos
                            each.save()
                        else:
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
        except:
            pass
        try:
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()
            reg7 = First.objects.filter(session=session, student=student)[0]
            if value == 1:
                reg7.value = 1
                reg7.save()
        except:
            pass

        return redirect('firsts')
    return render(request, 'result/firsts_confirm_delete.html', {'first': first})

@login_required
def deleteAdminFirst(request, id):
    first = First.objects.get(id=id)
    obj = get_object_or_404(First, id=id)
    session = first.session
    student = first.student
    subject = first.subject
    reg = First.objects.get(session=session, student=student, subject=subject)
    old_total = reg.total
    value = reg.value
    if request.method =="POST":
        obj.delete()
        try:
            reg1 = First.objects.filter(session=session, subject=subject)[0]
            reg1.subject_total = reg1.subject_total - old_total
            reg1.save()
        except:
            pass
        try:
            reg2 = First.objects.filter(session=session, subject=subject)[0]
            reg4 = First.objects.filter(session=session, subject=subject)
            n = reg4.count()
            d = round((reg2.subject_total/n),2)
            subject_position = []
            subject_pos = 0

            for each in reg4:
                each.subject_total = reg2.subject_total
                each.subject_avg = d
                each.grade = reg2.grade()
                each.save()
            for each in reg4:
                for i in range(len(subject_position)):
                    if subject_position[i] == each.total:
                        if i in range (10, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (11, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (12, len(subject_position), 100):
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (0, len(subject_position), 10):
                            subject_pos = str(i + 1) + "st"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (1, len(subject_position), 10):
                            subject_pos = str(i + 1) + "nd"
                            each.subject_pos = subject_pos
                            each.save()
                        elif i in range (2, len(subject_position), 10):
                            subject_pos = str(i + 1) + "rd"
                            each.subject_pos = subject_pos
                            each.save()
                        else:
                            subject_pos = str(i + 1) + "th"
                            each.subject_pos = subject_pos
                            each.save()
        except:
            pass
        try:
            reg6 = First.objects.filter(session=session, student=student)
            m = reg6.count()
            all_total = First.objects.filter(session=session, student=student).aggregate(Sum('total'))['total__sum']
            cum_perc = round((all_total/m),2)
            for each in reg6:
                each.cumulative = all_total
                each.cum_perc = cum_perc
                each.static_class = str(each.student.classe)
                each.save()
            reg7 = First.objects.filter(session=session, student=student)[0]
            if value == 1:
                reg7.value = 1
                reg7.save()
        except:
            pass

        return redirect('admin_firsts')
    return render(request, 'result/firsts_admin_confirm_delete.html', {'first': first})

@login_required
def showFirstsPay(request):
    context = {}
    filtered_firsts = FirstFilterPay(
        request.GET,
        queryset = First.objects.filter(value=1)
    )
    context['filtered_firsts'] = filtered_firsts
    paginated_filtered_firsts = Paginator(filtered_firsts.qs, 10)
    page_number = request.GET.get('page')
    firsts_page_obj = paginated_filtered_firsts.get_page(page_number)
    context['firsts_page_obj'] = firsts_page_obj
    total_firsts = filtered_firsts.qs.count()
    context['total_firsts'] = total_firsts
    return render(request, 'result/first_pay.html', context=context)

def updateFirstPay(request, id):
    first = First.objects.get(id=id)
    form = FirstFormPay(instance=first)
    if request.method=='POST':
        form = FirstFormPay(request.POST, instance=first)
        if form.is_valid():
            form.save()
            session = form.cleaned_data.get('session')
            student = form.cleaned_data.get('student')
            reg = First.objects.get(id=id)
            reg.student = student
            student_first_name = student.first_name
            student_last_name = student.last_name
            student_email = student.email
            reg.save()
            reg1 = First.objects.filter(session=session, student=student)
            for each in reg1:
                each.school_fees = reg.school_fees
                each.save()

            messages.success(request, "The student's payment has been modified successfully")
            return redirect('firsts_pay')
    return render(request, 'result/payment_update_first.html', {'form': form, 'first':first})
