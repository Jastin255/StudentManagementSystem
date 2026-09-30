from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from students.forms import StudentForm,ResultForm
from students.models import Student,Employee, Attendance, Fee, Result

from django.shortcuts import render, redirect
from .models import Course, Student
from .forms import StudentForm


def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)

            course_id = request.POST.get('course')

            if course_id and course_id != 'course_id' and course_id.isdigit():
                student.course = Course.objects.get(id=int(course_id))
            else:
                student.course = None

            student.save()
            return redirect('register')
    else:
        form = StudentForm()

    return render(request, 'students/registration.html', {'form': form})
def login_page(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'administrator':
            return render(request, 'students/administrator_login.html')
        elif user_type == 'employee':
            return render(request, 'students/employee_login.html')
        elif user_type == 'student':
            return render(request, 'students/student_login.html')
    return render(request, 'students/login.html')

def administrator_login(request, admin=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user is admin:
            login(request, user)
            return redirect('/admin/')
    return render(request, 'students/administrator_login.html')
def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/employee/dashboard/')
    return render(request, 'students/employee_login.html')

@login_required
def employee_dashboard(request):
    return render(request, 'students/employee_dashboard.html')
@login_required
def employee_logout(request):
    logout_student(request)
    return redirect('login_page')
def attendance(request):
    return render(request, 'students/attendance.html')
def mark_attendance(request):
    return render(request, 'students/mark_attendance.html')
def view_attendance(request):
    attendances = Attendance.objects.all()
    return render(
        request,'students/view_attendance.html',
        {'attendances': attendances}
    )
def fees_management(request):
    return render(
        request,'students/fees_management.html')


def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            return render(request, 'students/student_login.html', {'error': 'Invalid credentials'})

    return render(request, 'students/student_login.html')


@login_required(login_url='/student/login/')
def student_dashboard(request):
    return render(request, 'students/dashboard.html')


@login_required(login_url='/student/login/')
def student_logout(request):
    logout_student(request)
    return redirect('login_page')


def record_payment(request):
    if request.method == 'POST':
        try:
            registration_number = request.POST.get('registration_number')
            amount = request.POST.get('amount')
            payment_method = request.POST.get('payment_method')
            transaction_number = request.POST.get('transaction_number')
            receipt = request.FILES.get('receipt')

            student = Student.objects.get(registration_number=registration_number)
            Fee.objects.create(
                student=student,
                amount=amount,
                payment_method=payment_method,
                transaction_number=transaction_number,
                receipt=receipt
            )

            records = Fee.objects.all()
            return render(
                request,
                'students/record_payment.html',
                {'message': 'Payment recorded successfully!', 'records': records}
            )
        except Student.DoesNotExist:
            records = Fee.objects.all()
            return render(
                request,
                'students/record_payment.html',
                {'error': 'Student not found!', 'records': records}
            )
    records = Fee.objects.all()
    return render(request, 'students/record_payment.html', {'records': records})
def view_fees(request):
    payments = Fee.objects.all()
    return render(
               request,'students/view_fees.html', {'payments':payments}
)
def verify_payments(request):
    payments = Fee.objects.all()
    return render(request, 'students/verify_payments.html', {'payments':payments}
)
def verify_payment(request,payment_id):
    payment = Fee.objects.get(id=payment_id)
    payment.status = 'Verified'
    payment.save()
    return redirect('verify_payments')
@login_required
def record_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_result')
    else:
        form = ResultForm()
    return render(request, 'students/view_results.html', {'form': form})
@login_required
def view_results(request):
    results = Result.objects.all()
    return render(request,'students/view_results.html',{'results': results})
@login_required
def notifications(request):
    return render(request, 'students/notifications.html')
@login_required

def my_profile(request):
    return render(request, "students/sprofile.html")
def my_course(request):
    return render(request, "students/scourse.html")
def my_result(request):
    return render(request, "students/sresult.html")
def my_attendance(request):
    return render(request, "students/sattendance.html")
def my_fee(request):
    return render(request, "students/sfees.html")
def logout_student(request):
    return render(request, "students/slogout.html")