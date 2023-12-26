from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"index.html")

def show_tasks(request):
    return render(request,"tasks.html")