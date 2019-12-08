import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse('Two Index')


def add_student(request):
    for i in range(10):
        student = Student()
        student.s_name = f'Jerry{i}'
        student.s_age = random.randint(10, 100)
        student.save()
    return HttpResponse("Add success")


def student_list(request):
    students = Student.objects.filter(s_age__gt=20).filter(s_age__lt=50)
    context = {
         "students": students
    }
    return render(request, 'personlist.html', context=context)