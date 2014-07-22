from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField()
    pokedex_id = models.PositiveSmallIntegerField()
    team = models.ForeignKey(Team, null=True, blank=True)

    def __unicode__(self):
        return self.name

