from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.forms import StudentForm
# Create your views here.

def retrieve_view(request):
    stud=Student.objects.all()
    return render(request,'crudapp/index.html',{'student':stud})
def create_view(request):
    form = StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/stud')
    return render(request,'crudapp/create.html',{'form':form})
def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/stud')
def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/stud')
    return render(request,'crudapp/update.html',{'student':student})
    
    
    
    
    
    