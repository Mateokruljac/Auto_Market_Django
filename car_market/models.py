from django.db import models

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=30)
    
    def  __str__(self):
        return self.title # vratit će nam naziv umjesto "objekt"

class Car (models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    fuel = models.CharField(max_length=30)
    km = models.IntegerField()
    engine_volume = models.IntegerField()
    #svaki put kada izbrišemo brand mora se izbrisati i auto
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    