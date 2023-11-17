from rest_framework import serializers
from user_profile.models import Profile
from courses.models import Course
from user_profile.models import UserCourse


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    purchase_date = serializers.DateTimeField(read_only=True)
    is_completed = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserCourse
        fields = '__all__'