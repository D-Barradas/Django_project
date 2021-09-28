from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name="home"),
    ### <str:pk> is a dynamic value , a string , pk = primeary key it has to be also in the definition 
    path('projects/<str:pk>/',  views.projects, name="projects")
   
 ]