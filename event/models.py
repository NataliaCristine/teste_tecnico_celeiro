from django.db import models
import uuid

class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=255)
    
    sport = models.CharField(max_length=255)
    localization = models.ForeignKey('localization.Localization',on_delete=models.CASCADE,related_name='localization', null=True)
    users = models.ManyToManyField('user.User', related_name='users',null=True)
    game = models.ForeignKey('game.Game',related_name='game',on_delete=models.CASCADE,null=True)

    users_list = []

    def __hash__(self) -> int:
        return hash((self.name, self.game.uuid))

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.game.uuid == __o.game.uuid