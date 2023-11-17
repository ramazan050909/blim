from rest_framework.viewsets import ModelViewSet
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions.permissions import IsOwnerOrIsAdminUser


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer



    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()