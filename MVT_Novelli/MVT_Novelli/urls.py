from django.contrib import admin
from django.urls import path

from family.views import AddRelative, FamList, AddPet, PetList, AddVehicle, V_List
from .views import index


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
   
    path('fam-list/', FamList),
    path('fam-list/add-member', AddRelative),
       
    path('pet-list/', PetList),
    path('pet-list/add-pet', AddPet),
    
    path('v-list/', V_List),
    path('v-list/add-vehicle', AddVehicle),
    ]