from django.shortcuts import render, redirect
from reg_page.models import student, course

def home1(request):
    return render(request, 'homepage.html')

def studentlist(request):
    students = student.objects.all()
    return render(request, 'studentlist.html', {'student_list': students})

def courselist(request):
    courses = course.objects.all()
    return render(request, 'courselist.html', {'course_list': courses})

def register(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')
        selected_student = student.objects.get(id=student_id)
        selected_course = course.objects.get(id=course_id)
        selected_student.enrollment.add(selected_course)
        return redirect('/enrolledlist/')
    students = student.objects.all()
    courses = course.objects.all()
    return render(request, 'register.html', {'student_list': students, 'course_list': courses})

def enrolledStudents(request):
    course_list = course.objects.all()
    student_list = None
    selected_course = None
    if request.method == "POST":
        course_id = request.POST.get('course')
        selected_course = course.objects.get(id=course_id)
        student_list = selected_course.students.all()
    return render(request, 'enrolledlist.html', {
        'Course_List': course_list,
        'student_list': student_list,
        'course': selected_course
    })

