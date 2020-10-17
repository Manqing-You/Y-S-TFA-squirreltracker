from django.shortcuts import render
from .models import sightings
#from django.http import HttpResponse
from .forms import sightingsform
from django.shortcuts import redirect

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
    sighting=sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
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

