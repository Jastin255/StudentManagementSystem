from django.contrib import admin

# Register your models here.
from .models import Student,Employee,Attendance,Fee,Result,Course,Subject
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Fee)
admin.site.register(Result)
admin.site.register(Course)
admin.site.register(Subject)

