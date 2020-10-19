from django.shortcuts import render,get_object_or_404
from .models import sightings
from django.http import HttpResponse
from .forms import sightingsform
from django.shortcuts import redirect
from django.db.models import Avg

def details(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)


def list_all(request):
    mylist_ = sightings.objects.all()
    fields = ['Unique_Squirrel_ID','Date','Shift','See the details']
    context = {
            'mylist_':mylist_,
            'fields':fields,
            }
    return render(request, 'sightings/list_all.html', context)
	

def update(request,Unique_Squirrel_ID):
    sighting=get_object_or_404(sightings,Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        form = sightingsform(request.POST,instance=sighting)
        if form.is_valid():
            form.save()
            myinfo=sightings.objects.all()
            context={'myinfo':myinfo,}
            return render(request,'sightings/list_all.html',context)
    else:
        form = sightingsform(instance=sighting)
    context = {'form':form}
    return render(request, 'sightings/update.html',context)



def create_squirrel(request):
    if request.method == 'POST':
        form = sightingsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = sightingsform()

    context = {'form':form,}
    return render(request, 'sightings/add.html', context)

def stats(request):
    # LAT and LONG Average
    Lat_aver = sightings.objects.aggregate(Latitude=Avg('Latitude'))
    Long_aver= sightings.objects.aggregate(Longitude=Avg('Longitude'))
    biglat=sightings.objects.all().filter(Latitude__gte=40.78).count()
    smalllat=sightings.objects.all().filter(Latitude__lt=40.78).count()
    biglong=sightings.objects.all().filter(Longitude__gte=-73.97).count()
    smalllong=sightings.objects.all().filter(Longitude__lt=-73.97).count()
    #return a dictionary

    # Time
    AM_num = sightings.objects.all().filter(Shift='AM').count()
    PM_num = sightings.objects.all().filter(Shift='PM').count()

    #Basics
    # Age
    Juvenile_num = sightings.objects.all().filter(Age='Juvenile').count()
    Adult_num = sightings.objects.all().filter(Age='Adult').count()

    # Primary_Fur_Color
    Black_num = sightings.objects.all().filter(Primary_Fur_Color='Black').count()
    Gray_num = sightings.objects.all().filter(Primary_Fur_Color='Gray').count()
    Cinnamon_num = sightings.objects.all().filter(Primary_Fur_Color='Cinnamon').count()

    # Location
    Above_Ground_num = sightings.objects.all().filter(Location='Above Ground').count()
    Ground_Plane_num = sightings.objects.all().filter(Location='Ground Plane').count()

    # Behaviors
    Run_true = sightings.objects.all().filter(Running=True).count()
    Run_false = sightings.objects.all().filter(Running=False).count()
    Chasing_true = sightings.objects.all().filter(Chasing=True).count()
    Chasing_false = sightings.objects.all().filter(Chasing=False).count()
    Climbing_true = sightings.objects.all().filter(Climbing=True).count()
    Climbing_false = sightings.objects.all().filter(Climbing=False).count()
    Eating_true = sightings.objects.all().filter(Eating=True).count()
    Eating_false = sightings.objects.all().filter(Eating=False).count()
    Foraging_true = sightings.objects.all().filter(Foraging=True).count()
    Foraging_false = sightings.objects.all().filter(Foraging=False).count()


    context = {
            'Allnumber':sightings.objects.all().count(),
	    'Lat_aver':Lat_aver,
	    'Long_aver':Long_aver,
            'biglat':biglat,
            'smalllat':smalllat,
            'biglong':biglong,
            'smalllong':smalllong,
            'Shift': {'AM': AM_num,'PM': PM_num},
            'Age': {'Juvenile': Juvenile_num, 'Adult': Adult_num},
            'Primary_Fur_Color': {'Black':Black_num, 'Gray':Gray_num, 'Cinnamon':Cinnamon_num},
            'Location': {'Above_Ground':Above_Ground_num, 'Ground_Plane':Ground_Plane_num},
            'Running': {'True':Run_true, 'False':Run_false},
	    'Chasing': {'True':Chasing_true, 'False':Chasing_false},
	    'Climbing': {'True':Climbing_true, 'False':Climbing_false},
	    'Eating': {'True':Eating_true, 'False':Eating_false},
	    'Foraging': {'True':Foraging_true, 'False':Foraging_false},
            }
    return render(request, 'sightings/stats.html', {'context':context})
