from django.shortcuts import render
from .models import Tasks
# Create your views here.

def home(request):
    if request.method == "POST":
        taskTitle = request.POST["title"]
        taskDesc = request.POST["description"]
        taskDetails = Tasks(taskTitle=taskTitle,taskDesc=taskDesc)
        taskDetails.save()
        print("The data has been written to the database successfully")
    return render(request,"index.html")

def show_tasks(request):
    return render(request,"tasks.html")