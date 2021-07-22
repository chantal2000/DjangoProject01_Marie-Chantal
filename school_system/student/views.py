from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.shortcuts import render

# Create your views here.
def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_student.htm",{"form":form})

