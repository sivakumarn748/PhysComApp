from django.db import models
import uuid

# Create your models here.

class User(models.Model) :
    name = models.CharField(primary_key=True, max_length=255, null=False, unique=True)
    password = models.CharField(max_length=16, null=False)
    sessid = models.UUIDField(default=uuid.uuid4, unique=True)

    @property
    def sess_id(self) :
        return str(sessid)

    def __str__(self):
        return self.name
    