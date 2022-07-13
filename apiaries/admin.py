from django.contrib import admin
from apiaries import models
from chat.models import Message

admin.site.register(models.Apiary)
admin.site.register(Message)