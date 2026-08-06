# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Employee

def home(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    search = request.GET.get("search")
    dept = request.GET.get("department")

    if search:
        employees = employees.filter(name__icontains=search)
    if dept:
        employees = employees.filter(department_id=dept)

    return render(request, "home.html", {"employees": employees, "departments": departments})

def departments(request):
    if request.method == "POST":
        Department.objects.create(name=request.POST.get("name"))
        return redirect("departments")

    return render(request, "departments.html", {"departments": Department.objects.all()})

def employees(request):
    if request.method == "POST":
        dept = Department.objects.get(id=request.POST.get("department"))
        Employee.objects.create(
            name=request.POST.get("name"),
            emp_id=request.POST.get("emp_id"),
            email=request.POST.get("email"),
            department=dept,
            salary=request.POST.get("salary")
        )
        return redirect("employees")

    return render(request, "employees.html", {
        "employees": Employee.objects.all(),
        "departments": Department.objects.all()
    })

def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        emp.name = request.POST.get("name")
        emp.emp_id = request.POST.get("emp_id")
        emp.email = request.POST.get("email")
        emp.department = Department.objects.get(id=request.POST.get("department"))
        emp.salary = request.POST.get("salary")
        emp.save()
        return redirect("employees")

    return render(request, "employees.html", {
        "employee": emp,
        "employees": Employee.objects.all(),
        "departments": Department.objects.all()
    })

def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect("employees")
