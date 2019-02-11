from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.apps import apps as django_apps
from django.template.loader import render_to_string
Teacher = django_apps.get_model('School', 'Teacher')
Student = django_apps.get_model('School', 'Student')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return redirect("/login/")
    return redirect("/login/")

@login_required
def my_students(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    print("teacher:", len(teacher.students.all()))
    print(teacher.students.all())
    return render(request, 'my_students.html', {'students' : teacher.students.all()})
