from django.db import models
import uuid

class Localization(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=255)

    def __hash__(self) -> int:
        return hash(self.city)

    def __eq__(self, __o: object) -> bool:
        return self.city == __o.city
    