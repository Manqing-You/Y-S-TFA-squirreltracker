from django.shortcuts import render
from sightings.models import sightings
def mymap(request):
    mylist=sightings.objects.all()[:100]
    context={'mylist':mylist,}
    return render(request,'map/map.html',context)
# Create your views here.
