from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, to_field='title')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Certificate for {self.user.username} - {self.course.title}"