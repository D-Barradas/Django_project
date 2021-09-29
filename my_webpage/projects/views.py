from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request, pk):
    # return HttpResponse(content="Here is a project " + str(pk))
    return render(request,"projects/projects.html")

def single_project(request):
    return render(request,"projects/single_project.html")

def homepage(request):
    return HttpResponse(content="This is homepage")
