from rest_framework import routers 
from courses.views import CourseViewSet, ProfessionViewSet

router = routers.DefaultRouter()

router.register("courses", CourseViewSet, "courses")

router.register("profession", ProfessionViewSet, "profession")

urlpatterns = router.urls
