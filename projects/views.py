from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Project, Task

def dashboard_view(request):
    teams = Team.objects.filter(owner=request.user)
    projects = Project.objects.filter(team__owner=request.user).order_by('-id')[:10]
    tasks = Task.objects.filter(project__team__owner=request.user).order_by('-id')[:10]
    return render(request, 'projects/dashboard.html',{
        'teams':teams, 'projects': projects, 'tasks' : tasks
    })    


