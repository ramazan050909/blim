from rest_framework.viewsets import ModelViewSet
from courses.models import Profession, Course
from courses.serializers import CourseSerializer, ProfessionSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions.permissions import IsOwnerOrIsAdminUser
from rest_framework.response import Response
from rest_framework import status


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ProfessionViewSet(ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProfessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()