from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
class sightings(models.Model):
    Latitude=models.FloatField(
            null=True,blank=True,
            help_text=_('Latitude'),
    )
    Longitude=models.FloatField(
            null=True,blank=True,
            help_text=_('Longitude'),
    )
    Unique_Squirrel_ID=models.CharField(
            max_length=20,
            help_text=_('Unique Squirrel ID'),
    )
    PM='PM'
    AM='AM'
    Shift_choices=(
            (PM,'PM'),
            (AM,'AM'),
    )
    Shift=models.CharField(
            max_length=20,
            blank=True,
            choices=Shift_choices,
    )
    Date=models.DateField(
            help_text=_('Date'),
            null=True,
            blank=True,
    )
    adult='adult'
    juvenile='juvenile'
    other='other'
	Age_Choices=(
            (adult,'adult'),
            (juvenile,'juvenile'),
            (other,'other'),
    )
    Age=models.CharField(
            max_length=10,
            choices=Age_Choices,
            blank=True,
    )
    gray='gray'
    cinnamon='cinnamon'
    black='black'
    other='other'
    Fur_color_choices=(
            (gray,'gray'),
            (cinnamon,'cinnamon'),
            (black,'black'),
            (other,'other'),
    )
    Primary_Fur_Color=models.CharField(
            max_length=20,
            choices=Fur_color_choices,
            blank=True,
            help_text=_('Primary Fur Color'),
    )
    ground_plane='ground plane'
    above_ground='above ground'
    Location_choices=(
            (ground_plane,'ground plane'),
            (above_ground,'above ground'),
            (other,'other'),
    )
	Location=models.CharField(
            max_length=20,
            choices=Location_choices,
            blank=True,
    )
    Specific_location=models.CharField(
            max_length=200,
            help_text=_('Specific location'),
            blank=True,
    )
    Running=models.BooleanField(blank=True)
    Chasing=models.BooleanField(blank=True)
    Climbing=models.BooleanField(blank=True)
    Eating=models.BooleanField(blank=True)
    Foraging=models.BooleanField(blank=True)
    Other_Activities=models.CharField(max_length=200,blank=True)
    Kuks=models.BooleanField(blank=True)
    Quaas=models.BooleanField(blank=True)
    Moans=models.BooleanField(blank=True)
    Tail_flags=models.BooleanField(blank=True)
    Tail_twitches=models.BooleanField(blank=True)
    Approaches=models.BooleanField(blank=True)
    Indifferent=models.BooleanField(blank=True)
    Runs_from=models.BooleanField(blank=True)
	
    def __str__(self):
        return self.Unique_Squirrel_ID
		
    def getattrlist():
        return [i.name for i in sightings._meta.fields]