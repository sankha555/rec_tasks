from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def enter_stud(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return redirect('view_studs')

    else:
        form = StudentForm()

    return render(request, 'results/enter_stud.html', {'form':form})

def view_studs(request):

    studs = Student.objects.all()
    count = Student.objects.count()

    return render(request, 'results/view_studs.html', {'studs':studs, 'count':count})




# Create your views here.
