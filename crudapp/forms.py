from django import forms
from crudapp.models import Student

# Register your models here.
class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= '__all__' 
