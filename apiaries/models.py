from django.db import models
from users.models import User


# Create your models here.

class Apiary(models.Model):
    name = models.CharField(max_length=55)
    user = models.ForeignKey(User, related_name='apiary', on_delete=models.CASCADE)
    isHidden = models.BooleanField(default=True)
    status = models.CharField(max_length=55)
    location = models.JSONField()

    def __str__(self):
        return f'{self.name}:{self.user.email}'

