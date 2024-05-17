from django.shortcuts import render

from result.models import student


def home(request):
    students=student.objects.all()
    context={
        'students':students,
    }
    return render(request,'home.html',context)