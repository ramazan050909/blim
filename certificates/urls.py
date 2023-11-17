from rest_framework import routers
from certificates.views import CertificateViewSet

router = routers.DefaultRouter()

router.register("certificates", CertificateViewSet, "certificates")

urlpatterns = router.urls 