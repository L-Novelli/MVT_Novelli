from django.db import models

class Relatives(models.Model):
    name  = models.CharField(max_length=100)
    age = models.FloatField()
    work = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    
    
class Pets(models.Model):
    PetRace = models.CharField(max_length=100)
    Age = models.FloatField()
    Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Vehicles(models.Model):
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) 