from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=30)
    
    def  __str__(self):
        return self.title # vratit će nam naziv umjesto "objekt"

class Car (models.Model):
    name = models.CharField(max_length=30,blank = False) #required
    year = models.IntegerField(default= 0, blank = False,)
    fuel = models.CharField(max_length=30)
    km = models.IntegerField(default= 0, blank = False)
    engine_volume = models.IntegerField()
    #svaki put kada izbrišemo brand mora se izbrisati i auto
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE,blank = False)
 