from django.urls import path, include
from .views import dashboard_view
from rest_framework.routers import DefaultRouter
from .api_views import TeamViewSet, ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'api/teams', TeamViewSet)       # /projects/api/teams/
router.register(r'api/projects', ProjectViewSet) # /projects/api/projects/
router.register(r'api/tasks', TaskViewSet)       # /projects/api/tasks/

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),  # painel web
]

# expõe as rotas da API
urlpatterns += router.urls
