from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    student_list = []
    students = Student.objects.prefetch_related('teacher').order_by('group')
    for student in students:
        student_list.append(student)
    # teacher_list = []
    # teachers = Teacher.students.all()
    # for teacher in teachers:
    #     teacher_list.append(teacher)
    # context = {'object_list': student_list, 'teachers': teachers}
    context = {'object_list': student_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)
