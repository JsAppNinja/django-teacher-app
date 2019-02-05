from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
Teacher = django_apps.get_model('School', 'Teacher')
Student = django_apps.get_model('School', 'Student')


class UserAdmin(admin.ModelAdmin):
    list_display_links = ('username', 'email')
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    fields = ('username', 'email', 'is_staff', 'is_superuser')


class TeacherAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'email_address')
    fields = ('first_name', 'last_name', 'email_address', 'honorofic_title', 'students')


class StudentAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'grade_level', 'date_of_birth', 'student_id')
    fields = ('first_name', 'last_name', 'grade_level', 'date_of_birth', 'student_id', 'teachers')


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)




