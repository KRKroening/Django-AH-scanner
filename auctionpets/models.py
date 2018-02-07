from django.db import models


# Create your models here.


class Pets(models.Model):
    creatureId = models.IntegerField()
    speciesId = models.IntegerField(default=0)
    creatureName = models.CharField(max_length=25)
    collected = models.BooleanField(default=0)


    def __str__(self):
        return self.creatureName

    def isCollected(self):
        return "True" if self.collected == 0 else "False"

class AhPets(models.Model):
    speciesId = models.IntegerField(default=0)
    creatureId = models.IntegerField(default=0)
    creatureName = models.CharField(max_length=25)
    cost = models.TextField() #In copper
    time_left = models.TextField()

