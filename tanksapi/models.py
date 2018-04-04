from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Map(models.Model):
    name = models.CharField("Map Name", max_length=80)
    # if the user is deleted, then the foreign key here will be set to null, not deleting the map
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField("Created")
    thumbnail_url = models.URLField()
    terrain = models.TextField("terrain")
