from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from students import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/', views.student_registration, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('login/administrator/', views.administrator_login, name='administrator_login'),
    path('login/employee/', views.employee_login, name='employee_login'),
    path('student/student_login/', views.student_login, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/logout/', views.employee_logout, name='employee_logout'),
    path('attendance/',views.attendance,name='attendance'),
    path('attendance/mark/', views.mark_attendance, name='attendance_mark'),
    path('attendance/view/', views.view_attendance, name='view_attendance'),
    path('fees/',views.fees_management, name='fees_management'),
    path('fees/record/', views.record_payment, name='record_payment'),
    path('fees/view/', views.view_fees, name='view_fees'),
    path('fees/verify/',views.verify_payments,name='verify_payments'),
    path('fees/verify/<int:payment_id>/',views.verify_payment,name='verify_payment'),
    path('results/record/', views.record_result, name='record_result'),
    path('results/view/', views.view_results, name='view_results'),
    path('notifications/',views.notifications,name='notifications'),
    path('student/login/', views.student_login, name='student_login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
   path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student/profile/", views.my_profile, name="my_profile"),
    path("student/course/", views.my_course, name="my_course"),
    path("student/result/", views.my_result, name="my_result"),
    path("student/attendance/", views.my_attendance, name="my_attendance"),
    path("student/logout/", views.logout_student, name="logout_student"),
    path('',include('students.urls')),
    path('scourse/', views.my_course, name="course"),
    path('sfees/', views.my_fee, name="my_fee"),
    path('student/sresult/', views.my_result, name="result"),
    path('sattendence/', views.my_attendance, name="attendance"),
    path('slogout/',views.logout_student, name="logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)