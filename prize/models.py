from django.db import models
import uuid

class Prize(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medal = models.CharField(max_length=255,null=True)
    event = models.ForeignKey('event.Event',related_name='prize',on_delete=models.CASCADE,null=True)
    user = models.ForeignKey('user.User',related_name='prize',on_delete=models.CASCADE,null=True)
