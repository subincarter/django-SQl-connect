from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def connect(request):
    # stud=student.objects.all()
    return render(request,'conn.html',{'stud':stud})