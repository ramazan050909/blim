from rest_framework import routers
from materials.views import MaterialViewSet


router = routers.DefaultRouter()

router.register('materials', MaterialViewSet, 'materials')

urlpatterns = router.urls