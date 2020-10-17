from django.urls import path
  
from . import views

app_name='sightings'

urlpatterns=[
        path('sightings/',views.list_all,name='list_all'),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update,name='update'),
        path('sightings/<str:Unique_Squirrel_ID>/details/',views.details,name='details'),
]

