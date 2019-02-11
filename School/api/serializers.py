from django.apps import apps as django_apps


from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, status

Teacher = django_apps.get_model('School', 'Teacher')
User = django_apps.get_model('School', 'User')
Student = django_apps.get_model('School', 'Student')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class StudentSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'last_name', 'grade_level', 'hobby', 'student_id'
        )


class TeacherSimpleSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Teacher
        fields = (
            'id', 'first_name', 'last_name', 'honorofic_title', 'user',
        )


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    students = StudentSimpleSerializer(many=True)

    class Meta:
        model = Teacher
        fields = (
            'id', 'first_name', 'last_name', 'honorofic_title', 'user', 'students',
        )


class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSimpleSerializer(many=True)

    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'last_name', 'grade_level', 'hobby', 'student_id', 'teachers'
        )





