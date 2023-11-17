from user_profile.views import ProfileViewSet, UserCourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("user_profile", ProfileViewSet, "user_profile")
router.register("user_course", UserCourseViewSet, "user_course")

urlpatterns = router.urls
