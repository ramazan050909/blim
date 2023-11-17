from django.db import models



class Material(models.Model):
    MATERIAL_TYPE_CHOICES = (
        ('video', 'Видео'),
        ('text', 'Текст'),
        ('assigment', 'Домашнее задание'),
    )


    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    profession = models.ForeignKey('courses.Profession', on_delete=models.CASCADE, to_field='title')
    is_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    content_type = models.CharField(max_length=20, choices=MATERIAL_TYPE_CHOICES)
    content_file = models.FileField(upload_to='files/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    homework = models.TextField(blank=True, null=True)
    test = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def __repr__(self):
        return f"{self.title} - {self.price:.0f}"
    

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'