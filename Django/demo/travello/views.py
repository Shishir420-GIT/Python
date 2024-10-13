# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def travello(request):
    dest_details = Destination(1,"Shishir","is smart","Someadress",40)
    return render(request,'travello.html',{"dest": dest_details})
