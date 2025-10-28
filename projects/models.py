from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self._name
    
    
class Project(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self._name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    done = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self._title
    