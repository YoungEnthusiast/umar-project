from django.urls import path
from . import views

urlpatterns = [
    path('staff/first-term/result', views.showFirsts, name='firsts'),
    path('a---n/first-term/result', views.showAdminFirsts, name='admin_firsts'),
    path('student/first-term/result', views.showFirstsUser, name='firsts_user'),
    path('staff/first-term/results', views.showFirsts2, name='firsts2'),
    path('a---n/first-term/results', views.showAdminFirsts2, name='admin_firsts2'),
    path('a---n/first-term/payments', views.showFirstsPay, name='firsts_pay'),
    path('staff/first-term/result-sheets', views.showFirsts3, name='firsts3'),
    path('a---n/first-term/result-sheets', views.showAdminFirsts3, name='admin_firsts3'),
    path('student/first-term/result-sheets', views.showFirsts3User, name='firsts3_user'),
    path('staff/first-term/result/update/<int:id>', views.updateFirst, name='first_update'),
    path('a---n/first-term/result/update/<int:id>', views.updateAdminFirst, name='admin_first_update'),
    path('staff/first-term/result/delete/<int:id>', views.deleteFirst),
    path('a---n/first-term/result/delete/<int:id>', views.deleteAdminFirst),
    path('staff/first-term/result/attitude-and-skills/<int:id>', views.updateFirstBeha, name='first_update_beha'),
    path('a---n/first-term/result/attitude-and-skills/<int:id>', views.updateAdminFirstBeha, name='admin_first_update_beha'),
    path('staff/first-term/add-result/<int:id>', views.addFirst, name='first'),
    path('first-term/report-sheets/<str:pk>/', views.showReportCt, name='show_report_ct'),
    path('first-term/report/<str:pk>/', views.showReportAdmin, name='show_report_admin'),
    path('first-term/report-sheet/<str:pk>/', views.showReportUser, name='show_report_user'),
    path('a---n/first-term/result/payment/<int:id>', views.updateFirstPay, name='first_update_pay'),
    ]
