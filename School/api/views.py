
from django.apps import apps as django_apps
from rest_framework import (
    viewsets, mixins, permissions, generics, status, exceptions)
from rest_framework.response import Response
from api import serializers as main_serializer
from django.shortcuts import get_object_or_404
from django.db.models import FieldDoesNotExist

Teacher = django_apps.get_model('School', 'Teacher')
Student = django_apps.get_model('School', 'Student')


class TeacherListView(generics.ListAPIView):
    serializer_class = main_serializer.TeacherSerializer
    queryset = Teacher.objects.all()
    # permission_classes = permissions.IsAuthenticated
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort', None)
        search_string = request.GET.get('search', None)
        try:
            Teacher._meta.get_field(sort)
            query_results = self.get_queryset().order_by(sort)
        except FieldDoesNotExist:
            query_results = self.get_queryset()
        if search_string != None:
            query_results = query_results.filter(last_name__icontains=search_string)
        serializer = self.serializer_class(query_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherRetriveView(generics.ListAPIView):
    serializer_class = main_serializer.TeacherSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        teacher_instance = get_object_or_404(Teacher, pk=id)
        serializer = self.serializer_class(teacher_instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentListView(generics.ListAPIView):
    serializer_class = main_serializer.StudentSerializer
    queryset = Student.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        type = request.GET.get('type', None)
        id = request.GET.get('id', None)
        sort = request.GET.get('sort')
        search_string = request.GET.get('search', '')
        if type == None:
            if id == None:
                try:
                    Student._meta.get_field(sort)
                    query_results = self.get_queryset().order_by(sort)
                except FieldDoesNotExist:
                    query_results = self.get_queryset()

                query_results = query_results.filter(last_name__icontains=search_string)

                serializer = self.serializer_class(query_results, many=True)
            else:
                student_instance = get_object_or_404(Student, pk=id)
                serializer = self.serializer_class(student_instance, many=False)
        elif type == 'teacher':
            teacher_instance = get_object_or_404(Teacher, id=id)
            try:
                Student._meta.get_field(sort)
                query_results = teacher_instance.students.order_by(sort)
            except FieldDoesNotExist:
                query_results = teacher_instance.students
            query_results = query_results.filter(last_name__icontains=search_string)
            serializer = self.serializer_class(query_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherStudentsListView(generics.ListAPIView):
    serializer_class = main_serializer.StudentSimpleSerializer
    queryset = ''
    def get(self, request, id):
        teacher_instance = get_object_or_404(Teacher, id=id)
        serializer = self.serializer_class(teacher_instance.students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
