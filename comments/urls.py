from rest_framework import routers
from comments.views import CommentViewSet, ComplaintViewSet, BlockedCommentViewSet

router = routers.DefaultRouter()

router.register('comments', CommentViewSet, 'comments')
router.register('complaints', ComplaintViewSet, 'complaints')
router.register('blocked_comments', BlockedCommentViewSet, 'blocked_comments')

urlpatterns = router.urls