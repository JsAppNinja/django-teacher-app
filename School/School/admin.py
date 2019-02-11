from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from django import forms
User = get_user_model()
Teacher = django_apps.get_model('School', 'Teacher')
Student = django_apps.get_model('School', 'Student')


class StudentForm(forms.ModelForm):
    hobby = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=Student.HOBBY_CHOICES)

    class Meta:
        model = Student
        exclude = []


class UserAdmin(UserAdmin):
    list_display_links = ('email',)
    list_display = ('email', 'is_staff', 'is_superuser',)


class TeacherAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name',)
    fields = ('first_name', 'last_name', 'honorofic_title', 'students', 'user',)


class StudentAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'grade_level', 'date_of_birth', 'student_id')
    fields = ('first_name', 'last_name', 'grade_level', 'date_of_birth', 'student_id', 'teachers', 'hobby',)
    form = StudentForm


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)

