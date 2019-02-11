from django.conf.urls import url
from api import views as core_view

urlpatterns = [
    url(r'^teachers/$', core_view.TeacherListView.as_view(), name='teacher-list'),
    url(r'^teachers/(?P<id>\w+)/$', core_view.TeacherRetriveView.as_view(), name='teacher-object'),
    url(r'^students/$', core_view.StudentListView.as_view(), name='student-list'),
]
