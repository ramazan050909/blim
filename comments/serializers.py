from rest_framework import serializers
from comments.models import Comment, Complaint, BlockedComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


class BlockedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedComment
        fields = '__all__'