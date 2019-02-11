# import datetime
# from django.apps import apps as django_apps
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps as django_apps
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete

from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(null=False, unique=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()


class Teacher(models.Model):

    MR, MRS, MS, DR, BLANK ='Mr', 'Mrs', 'Ms', 'Dr', ''
    HONORFIC_TITLE = (
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (BLANK, ''),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="User",
        on_delete=models.CASCADE,
        related_name='teacher', null=False)

    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)
    honorofic_title = models.CharField(
        max_length=3,
        choices=HONORFIC_TITLE,
        default=MR)
    students = models.ManyToManyField(settings.STUDENT_MODEL, related_name="teachers", blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    BAKING, CHESS, DRAWING, MUSIC, SPORTS = 'backing', 'chess', 'drawing', 'music', 'sports'
    HOBBY_CHOICES = (
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
    hobby = ArrayField(
        models.CharField(choices=HOBBY_CHOICES, max_length=10, blank=True, default=BAKING)
    )
    grade_level = models.IntegerField(choices=GRADE_LEVEL, default=1)
    student_id = models.CharField(blank=False, null=False, max_length=255)
    
    def __str__(self):
        return self.first_name +  " "  + self.last_name;


@receiver(pre_save, sender=User)
def UserName(sender, instance, **kwargs):
    try:
       instance.username = instance.email
    except Exception as e:
        print(str(e))
