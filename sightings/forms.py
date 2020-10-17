from .models import sightings

from django.forms import ModelForm

class sightingsform(ModelForm):
    class Meta:
        model=sightings
        fields="__all__"
