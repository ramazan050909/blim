from django.db import models
from django.contrib.auth.models import User 


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscriptions', to_field='username')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    base_subscription = models.BooleanField(default=False)
    pro_subscription = models.BooleanField(default=False)
    user_free_courses = models.PositiveIntegerField(default=0)
    has_mentor_feedback = models.BooleanField(default=False)
    has_acces_to_tests = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user.username} - с {self.start_date} по {self.end_date}'