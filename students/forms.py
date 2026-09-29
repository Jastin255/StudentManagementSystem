from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'registration_number',
            'full_name',
            'gender',
            'course',
            'year',
            'education_level',
            'department',
            'phone_number',
            'email',
        ]
from .models import Result
class ResultForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        empty_label="- Select Student registration_number -",
    )
    class Meta:
        model = Result
        fields = [
            'student',
            'subject',
            'cart_marks',
            'exam_marks',
            'total_marks',
            'semester',
            'grade',
            'academic_year',
        ]