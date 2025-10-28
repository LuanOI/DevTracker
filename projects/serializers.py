from rest_framework import serializers
from .models import Team, Project, Task

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'           