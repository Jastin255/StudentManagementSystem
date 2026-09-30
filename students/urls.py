from django.urls import path
from  . import views

urlpatterns = [path('register/', views.student_registration, name='student_registration'),
               path('login/', views.student_login, name='student_login'),
               path('admin_login/', views.administrator_login, name='admin_login'),
]