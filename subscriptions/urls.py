from rest_framework import routers
from subscriptions.views import SubscriptionViewSet


router = routers.DefaultRouter()

router.register("subscriptions", SubscriptionViewSet, "subscriptions")

urlpatterns = router.urls