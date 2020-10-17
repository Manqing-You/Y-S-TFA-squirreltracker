from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Squirrel(models.Model):
    """ squirrel model """
    def __str__(self):
        return "self.Unique_Squirrel_ID"
    def getattrlist():
        return [i.name for i in sightings._mata.fields]
    Latitude = models.FloatField(null=True, blank=True, verbose_name="latitude")
    Longtitude = models.FloatField(null=True, blank=True, verbose_name="longitude")
    Unique_squirrel_id = models.CharField(max_length=20,default="")
    Shift = models.CharField(max_length=20,default="")
    Date = models.DateField("date")
    Age = models.CharField(max_length=10,default="")
    Primary_Fur_Color = models.CharField(max_length=10,default="")
    Location = models.CharField(max_length=20,default="")
    Specific_Location = models.CharField(max_length=40,default="")
    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)
    Other_Activities = models.CharField(max_length=50,default="")
    Kuks = models.BooleanField(default=False)
    Quaas = models.BooleanField(default=False)
    Moans = models.BooleanField(default=False)
    Tail_flags = models.BooleanField(default=False)
    Tail_twitches = models.BooleanField(default=False)
    Approaches = models.BooleanField(default=False)
    Indifferent = models.BooleanField(default=False)
    Runs_from = models.BooleanField(default=False)
