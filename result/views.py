from django.shortcuts import get_object_or_404, render

from result.models import student

# Create your views here.
def student_details(request,pk):
    students=get_object_or_404(student,pk=pk)
    context={
        'students':students,
    }
    return render(request,'student_detail.html',context)