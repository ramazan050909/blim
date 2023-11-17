from rest_framework.viewsets import ModelViewSet
from comments.models import Comment, Complaint, BlockedComment
from comments.serializers import CommentSerializer, ComplaintSerializer, BlockedCommentSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions.permissions import IsOwnerOrIsAdminUser




class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ComplaintViewSet(ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class BlockedCommentViewSet(ModelViewSet):
    queryset = BlockedComment.objects.all()
    serializer_class = BlockedCommentSerializer


    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()