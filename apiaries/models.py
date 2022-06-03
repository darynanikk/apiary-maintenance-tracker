from django.db import models
from users.models import User


# Create your models here.

class Apiary(models.Model):
    name = models.CharField(max_length=55)
    user = models.ForeignKey(User, related_name='apiaries', on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=True)
    status = models.CharField(max_length=55, default="test")
    location = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.name}:{self.user.email}'
