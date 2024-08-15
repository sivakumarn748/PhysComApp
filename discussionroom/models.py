from django.db import models
import uuid

# Create your models here.

class Room(models.Model) :
    roomid = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, null=False)
    key = models.CharField(max_length=16, null=False)
    about = models.CharField(max_length=255, null=True)

    @property
    def invite_url (self) :
        return f"myurl/{str(self.roomid)}"

    def __str__(self):
        return self.name
    