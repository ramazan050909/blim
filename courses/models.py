from django.db import models
from django.core.exceptions import ValidationError
from materials.models import Material

class Profession(models.Model):
    title = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, to_field='title')
    materials = models.ManyToManyField(Material, related_name='courses',blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.is_free and not self.price:
            raise ValidationError('Price is required for non-free courses.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Perform validation before saving
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    def __repr__(self):
        return f"{self.title} - {self.price:.0f}"
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
