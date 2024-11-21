from projects.models import Project
from rest_framework import viewsets, permissions, filters
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Qué operaciones tiene permitido hacer
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
