from django.shortcuts import render
from .models import Tasks
# Create your views here.

def home(request):
    context = {
        "success": False,
        "name": "Arnab"
    }
    if request.method == "POST":
        taskTitle = request.POST["title"]
        taskDesc = request.POST["description"]
        taskDetails = Tasks(taskTitle=taskTitle,taskDesc=taskDesc)
        taskDetails.save()
        print("The data has been written to the database successfully")
        context = {
            "success": True
        }
    print(context)
    return render(request,"index.html",context)

def show_tasks(request):
    all_tasks = Tasks.objects.all()
    context = {
        "tasks": all_tasks
    }
    return render(request,"tasks.html",context)