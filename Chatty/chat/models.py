from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name.__str__()
    
class Message(models.Model):
    value = models.CharField(max_length=512)
    date = models.DateTimeField(default= datetime.now, blank=True)
    user = models.CharField(max_length=60)
    room = models.CharField(max_length=255)