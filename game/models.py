from django.db import models
import uuid

class Game(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    year = models.BigIntegerField()
    season= models.CharField(max_length=255)
    teams = models.ManyToManyField('team.Team', related_name='games',null=True)

    teams_list= []

    def __hash__(self) -> int:
        return hash((self.name,self.year))
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.year == __o.year
