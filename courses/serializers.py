from rest_framework import serializers
from courses.models import Course
from courses.models import Profession
from subscriptions.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


    def validate(self, data):
        # Получаем пользователя из контекста запроса
        user = self.context['request'].user

        # Проверяем, есть ли у пользователя активная подписка
        try:
            subscription = Subscription.objects.get(user=user, is_active=True)
        except Subscription.DoesNotExist:
            raise serializers.ValidationError("У вас нет активной подписки.")

        # Проверяем тип подписки и выполняем соответствующую логику
        if subscription.pro_subscription:
            return data

        if subscription.base_subscription and subscription.user_free_courses < 10:
            return data

        raise serializers.ValidationError("У вас нет доступа к этому курсу.")

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'