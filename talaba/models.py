from django.db import models
from django.contrib.auth.models import User

# Testlar uchun model yaratish
class TestNatija(models.Model):
    class Meta:
        verbose_name_plural = 'Test Natijalar'
        verbose_name = 'Test Natija'
    
    talaba = models.ForeignKey(User, on_delete=models.CASCADE)
    ball = models.IntegerField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.talaba} - {self.ball} ball'