from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def projects(request, pk):
    return HttpResponse(content="Here is a project " + str(pk))

def homepage(request):
    return HttpResponse(content="This is homepage")
