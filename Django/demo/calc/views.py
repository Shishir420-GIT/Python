from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html',{"name": "shishir"})


def add(request):
    # num1 = int(request.GET['num1'])
    # num2 = int(request.GET['num2'])
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2
    return render(request,'result.html',{"result": res})