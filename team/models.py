from django.db import models
import uuid

class Team(models.Model):
     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     name = models.CharField(max_length=255)
     ndc = models.CharField(max_length=255)
