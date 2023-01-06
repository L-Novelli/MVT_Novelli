from django.shortcuts import render
from django.http import HttpResponse


from family.models import Relatives, Pet, Vehicle
from family.forms import Family, Pets, Vehicles


def AddRelative(request):
    if request.method == 'GET':
        context = {
            'form': Family()
        }

        return render(request, 'addRelative.html', context=context)

    elif request.method == 'POST':
        form = Family(request.POST)
        if form.is_valid():
            Relatives.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                work=form.cleaned_data['work'],
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'addRelative.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Family()
            }
            return render(request, 'addRelative.html', context=context)

def AddPet(request):
    if request.method == 'GET':
        context = {
            'form': Pets()
        }

        return render(request, 'addPet.html', context=context)

    elif request.method == 'POST':
        form = Pets(request.POST)
        if form.is_valid():
            Pet.objects.create(
                Name=form.cleaned_data['Name'],
                Age=form.cleaned_data['Age'],
                PetRace=form.cleaned_data['PetRace'],
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'addPet.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Pets()
            }
            return render(request, 'addPet.html', context=context)

def AddVehicle(request):
    if request.method == 'GET':
        context = {
            'form': Vehicles()
        }

        return render(request, 'addVehicle.html', context=context)

    elif request.method == 'POST':
        form = Vehicles(request.POST)
        if form.is_valid():
            Vehicle.objects.create(
                Brand=form.cleaned_data['Brand'],
                Model=form.cleaned_data['Model'],
                Colour=form.cleaned_data['Colour'],
            )
            context = {
                'message': 'added successfully'
            }
            return render(request, 'addVehicle.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': Vehicles()
            }
            return render(request, 'addVehicle.html', context=context)


def FamList(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Family = Relatives.objects.filter(name__icontains=search) 
    else:
        all_Family = Relatives.objects.all()   
    context = {
        'Family':all_Family,
    }
    return render(request, 'Family.html', context=context)


def PetList(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Pets = Pets.objects.filter(name__icontains=search) 
    else:   
        all_Pets = Pets.objects.all()
    context = {
        'Pets':all_Pets,
    }
    return render(request, 'Pets.html', context=context)


def V_List(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_Vehicles = Vehicles.objects.filter(model__icontains = search) 
    else:   
        all_Vehicles = Vehicles.objects.all()  
    context = {
        'Vehicle':all_Vehicles,
    }
    return render(request, 'Vehicle.html', context=context)
