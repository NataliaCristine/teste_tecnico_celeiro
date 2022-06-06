from django.db import models
import uuid

class Measure(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heigth= models.IntegerField(null=True)
    wheight=models.IntegerField(null=True)
    age = models.CharField(max_length=255)
    user = models.ForeignKey('user.User',on_delete=models.CASCADE,related_name='measurements', null=True)

    def __hash__(self) -> int:
        return hash((self.age,self.user.id))

    def __eq__(self, __o: object) -> bool:
        return self.age == __o.age and self.user.id == __o.user.id