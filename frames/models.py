from django.db import models
from hives.models import Hive


# Create your models here.
class Frame(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE, related_name='frames')
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=55, default="test")
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    moveHistory = models.CharField(max_length=255)

    def __str__(self):
        print(f"frame of {self.type}")
