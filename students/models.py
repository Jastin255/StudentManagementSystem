from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.code + " - " + self.name
class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    registration_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    education_level = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    year = models.IntegerField(default=1)
    def __str__(self):
        return self.registration_number + " - " + self.full_name
class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    employee_no = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.employee_no + " - " + self.first_name
class Result(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subject = models.CharField(max_length=50)
    cart_marks = models.FloatField(default=0)
    exam_marks = models.FloatField(default=0)
    total_marks = models.FloatField(default=0)
    grade = models.CharField(max_length=5, blank=True)
    semester = models.CharField(max_length=50, blank=True)
    academic_year = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.student.registration_number+ " - " + self.course.code
class Attendance(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    date = models.DateField()
    status = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.student.registration_number} -{self.date}"
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    transaction_number = models.CharField(max_length=100, null=True, blank=True)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateField()
    description = models.CharField(
        max_length=200,
        blank=True
    )
    def __str__(self):
        return self.student.registration_number + " - " + str(self.amount)

