from django.shortcuts import render, redirect
from .forms import StudentForm


def home(request):
    return render(request, 'students/home.html')


def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {'form': form}
    )