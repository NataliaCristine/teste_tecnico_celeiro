
from pickle import TRUE
from django.db import models
import uuid

class User(models.Model):
    id = models.IntegerField(unique=TRUE,primary_key=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    team = models.ForeignKey('team.Team',on_delete=models.CASCADE,related_name='team', null=True)
