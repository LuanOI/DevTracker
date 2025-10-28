from rest_framework import viewsets, permissions
from .models import Team, Project, Task
from .serializers import teamSerializer, ProjectSerializer, TaskSerializer

class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return obj.owner ==request.user
        if hasattr(obj,'team'):
            return obj.team.owner ==request.user
        if hasattr(obj, 'project'):
            return obj.project.team.owner ==request.user
        return False

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = teamSerializer
    permissions_classes = [permissions.IsAuthenticated, IsOwnerOnly]
    queryset = Team.objects.all()
    
    def get_queryset(self):
        return Team.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOnly]
    queryset = Project.objects.all()
    
    def get_queryset(self):
        # só projetos dos times do usuário
        return Project.objects.filter(team__owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOnly]
    queryset = Task.objects.all()

    def get_queryset(self):
        # só tarefas de projetos do usuário
        return Task.objects.filter(project__team__owner=self.request.user)            
        
    