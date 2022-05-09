from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg-umar-ister', views.createAdFirst, name='account_ad_first'),
    path('reg-sta', views.createStaff, name='account_sta_first'),
    path('where-next/', views.loginTo),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('a---n-edit-profile', views.editProfileAdminFirst, name='profile_admin_first'),
    path('staff-edit-profile', views.editProfileStaffFirst, name='profile_staff_first'),
    path('student-edit-profile', views.editProfileStudentFirst, name='profile_student_first'),
    path('change-password', views.changePassword, name='change_password'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
    path('staff/students', views.showStudentsFirst, name='staff_students_first'),
    path('a---n/students', views.showStudentsFirst2, name='admin_students_first'),
    path('a---n/staffs', views.showStaffsFirst, name='staffs_first'),
    path('a---n/staffs/update/<int:id>', views.updateStaffsFirst, name='staff_update_first'),
    path('a---n/staffs/delete/<int:id>', views.deleteStaffFirst),
    path('a---n/students/delete/<int:id>', views.deleteStudentFirst),
    path('staff/students/<str:pk>/', views.showStudent, name='show_student'),
    path('a---n/students/<str:pk>/', views.showStudentAd, name='show_student_ad'),
    path('a---n/students/update/<int:id>', views.updateStudentsFirst, name='student_update_first'),
    path('a---n/staffs/<str:pk>/', views.showStaff, name='show_staff'),

    path('a---n-dashboard-first-term', views.showAdminBoardFirst, name='admin_board_first'),
    path('staff-dashboard-first-term', views.showStaffBoardFirst, name='staff_board_first'),
    path('student-dashboard-first-term', views.showStudentBoardFirst, name='student_board_first'),

    path('rumar', views.create, name='account'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('complete-registration', views.editProfile0, name='edit_profile0'),
    path('edit-profile', views.editProfile, name='edit_profile'),
    path('change-password', views.changePassword, name='change_password'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name='reset_password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'), name='password_reset_complete'),
]
