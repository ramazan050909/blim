from rest_framework.viewsets import ModelViewSet
from materials.models import Material

from materials.serializers import MaterialSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions.permissions import IsOwnerOrIsAdminUser


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()