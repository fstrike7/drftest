from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() # CRUD

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls