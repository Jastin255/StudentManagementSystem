from django.contrib import admin

# Register your models here.
from .models import Student,Employee,Attendance,Fee,Result
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Fee)
admin.site.register(Result)