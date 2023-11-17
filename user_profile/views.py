from rest_framework.viewsets import ModelViewSet
from djoser.views import UserViewSet as DjoserUserViewSet
from user_profile.models import Profile, UserCourse
from user_profile.serializers import ProfileSerializer, UserCourseSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions.permissions import IsOwnerOrIsAdminUser




class UserCourseViewSet(ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        user = self.request.user  # Получаем текущего пользователя
        profile = serializer.save(user=user)
        return profile
    
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()