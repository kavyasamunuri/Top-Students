from django.urls import path

from . import views


urlpatterns=[
    path('<int:pk>/',views.student_details,name='student_detail'),
]