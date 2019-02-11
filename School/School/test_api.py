from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.apps import apps as django_apps
from django.db import IntegrityError
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from django.contrib import auth

User = get_user_model()
Teacher = django_apps.get_model('School', 'Teacher')
Student = django_apps.get_model('School', 'Student')

class StudentTest(TestCase):
    def test_unique(self):
        #date_of_birth not-null integrity test
        with self.assertRaises(Exception) as raised:  # top level exception as we want to figure out its exact type
            Student.objects.create(first_name='student2', last_name="two", grade_level=11, hobby=['drawing', 'backing'], student_id="eqwe12@#34232$D1")
        self.assertEqual(IntegrityError, type(raised.exception))

class TeacherTest(TestCase):
    def test_login(self):
        email = "test_startup1@test.com"
        password = "password123"
        user = User.objects.create(
            email=email,
            password='password'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        teacher = Teacher.objects.create(first_name='hello', last_name='world', honorofic_title='Mr', user=user)

        assert teacher.id != None

class TestRelationShipe(TestCase):
    def test_relationshipe(self):
        email = "test_startup1@test.com"
        password = "password123"
        user = User.objects.create(
            email=email,
            password='password'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

        student = Student.objects.create(first_name='student2', date_of_birth='2019-02-16', last_name="two", grade_level=11, hobby=['drawing', 'backing'], student_id="eqwe12@#34232$D1")
        teacher = Teacher.objects.create(first_name='Teacher', last_name='relationshipe', honorofic_title='Mr', user=user)
        teacher.students.add(student)
        teacher.save()
        self.assertEqual(student.teachers.all()[0], teacher)
