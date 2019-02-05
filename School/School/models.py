# import datetime
# from django.apps import apps as django_apps
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.auth import get_user_model


# 1. Create three Models:
# Teacher: first_name, last_name, honorofic_title (select from Mr., Mrs., Ms., Dr., Blank), email_address, Unique Key: email_address
# Student: first_name, last_name, date_of_birth (datetime), grade_level (select from k, 1,2,...,12), hobby (multi-select from baking, chess, drawing, music, sports), student_id (business key, not-system generated), Unique Key: student_id
# Create a relationship so that a student can be associated with more than one teacher
#
# 2. A responsive UI with Admin views to CRUD the models and relationships such that, as an Admin I can log into a website and create, edit, read, delete
# Teachers and their relationships to students
# Students and their relationships to teachers
#
# 3. A responsive UI where as a Teacher I can view my students.

class User(AbstractUser):
    username = models.CharField(null=False, unique=True, max_length=255)
    email = models.EmailField(null=False, unique=True, max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Teacher(models.Model):

    MR, MRS, MS, DR, BLANK ='Mr', 'Mrs', 'Ms', 'Dr', ''
    HONORFIC_TITLE = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (BLANK, ''),
    )

    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    honorofic_title = models.CharField(
        max_length=3,
        choices=HONORFIC_TITLE,
        default=MR)
    email_address = models.EmailField(blank=False, null=False, unique=True, max_length=255)
    students = models.ManyToManyField(settings.STUDENT_MODEL, related_name="students", blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    BAKING, CHESS, DRAWING, MUSIC, SPORTS = 'backing', 'chess', 'drawing', 'music', 'sports'
    HOBBY = (
        (BAKING, 'baking'),
        (CHESS, 'chess'),
        (DRAWING, 'drawing'),
        (MUSIC, 'music'),
        (SPORTS, 'sports'),
    )

    GRADE_LEVEL = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
    )
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    date_of_birth = models.DateField(blank=False)
    grade_level = models.IntegerField(choices=GRADE_LEVEL, default=1)
    student_id = models.CharField(blank=False, null=False, max_length=255)
    teachers = models.ManyToManyField(settings.TEACHER_MODEL, related_name='teachers', blank=True)

    def __str__(self):
        return self.first_name +  " "  + self.last_name;
