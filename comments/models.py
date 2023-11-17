from django.db import models
from django.contrib.auth.models import User
from materials.models import Material

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    materials = models.ForeignKey(Material, related_name='comments', on_delete=models.CASCADE, to_field='title')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)  # Поле для указания, заблокирован ли комментарий

    def block(self):
        self.is_blocked = True
        self.save()

    def unblock(self):
        self.is_blocked = False
        self.save()

    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
class BlockedComment(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)




