# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment

def home(request):
    enrollments = Enrollment.objects.all()
    courses = Course.objects.all()
    search = request.GET.get("search")
    course = request.GET.get("course")

    if search:
        enrollments = enrollments.filter(student__name__icontains=search)
    if course:
        enrollments = enrollments.filter(course_id=course)

    return render(request, "home.html", {"enrollments": enrollments, "courses": courses})

def students(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            roll_number=request.POST.get("roll"),
            email=request.POST.get("email")
        )
        return redirect("students")

    return render(request, "students.html", {"students": Student.objects.all()})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll_number = request.POST.get("roll")
        student.email = request.POST.get("email")
        student.save()
        return redirect("students")

    return render(request, "students.html", {"student": student, "students": Student.objects.all()})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("students")

def courses(request):
    if request.method == "POST":
        Course.objects.create(
            name=request.POST.get("name"),
            course_code=request.POST.get("code"),
            credits=request.POST.get("credits")
        )
        return redirect("courses")

    return render(request, "courses.html", {"courses": Course.objects.all()})

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course.name = request.POST.get("name")
        course.course_code = request.POST.get("code")
        course.credits = request.POST.get("credits")
        course.save()
        return redirect("courses")

    return render(request, "courses.html", {"course": course, "courses": Course.objects.all()})

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect("courses")

def enrollment(request):
    if request.method == "POST":
        student = Student.objects.get(id=request.POST.get("student"))
        course = Course.objects.get(id=request.POST.get("course"))
        Enrollment.objects.create(
            student=student,
            course=course,
            semester=request.POST.get("semester")
        )
        return redirect("enrollment")

    return render(request, "enrollment.html", {
        "enrollments": Enrollment.objects.all(),
        "students": Student.objects.all(),
        "courses": Course.objects.all()
    })

def edit_enrollment(request, id):
    enrollment_obj = get_object_or_404(Enrollment, id=id)
    if request.method == "POST":
        enrollment_obj.student = Student.objects.get(id=request.POST.get("student"))
        enrollment_obj.course = Course.objects.get(id=request.POST.get("course"))
        enrollment_obj.semester = request.POST.get("semester")
        enrollment_obj.save()
        return redirect("enrollment")

    return render(request, "enrollment.html", {
        "enrollment": enrollment_obj,
        "enrollments": Enrollment.objects.all(),
        "students": Student.objects.all(),
        "courses": Course.objects.all()
    })

def delete_enrollment(request, id):
    enrollment_obj = get_object_or_404(Enrollment, id=id)
    enrollment_obj.delete()
    return redirect("enrollment")
