from django.shortcuts import render


from .models import Course, Student

def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses' : courses})

def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students' : students})



