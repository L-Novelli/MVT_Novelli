from django import forms

class Family(forms.Form):
    name  = forms.CharField(max_length=100)
    age = forms.FloatField()
    work = forms.BooleanField()
    
class Pets(forms.Form):
    PetRace = forms.CharField(max_length=100)
    Age = forms.FloatField()
    Name = forms.CharField(max_length=100)
    
class Vehicles(forms.Form):
    Brand = forms.CharField(max_length=100)
    Model = forms.CharField(max_length=100)
    Colour = forms.CharField(max_length=100)