from django.db import models
from apiaries.models import Apiary

# Create your models here.


class Hive(models.Model):
    color = models.CharField(default="", max_length=255)
    apiary = models.ForeignKey(Apiary, related_name="hives", on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    status = models.CharField(default="", max_length=255)
    bees_family = models.CharField(default="", max_length=255)
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.number}:{self.type}'