from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"index.html")

def show_tasks(request):
    return render(request,"tasks.html")