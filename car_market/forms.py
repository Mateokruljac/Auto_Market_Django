from django import forms
from .models import Car
from django.contrib.auth.models import User
class CarForms (forms.ModelForm):
    # mijenja način rada ili ponašanje, opcije...
    class Meta: # inner klasa kojom dodjeljujemo metapodatak -> odnosno sve što nije polje
         
        model = Car # model kojim se bavimo je Car
        fields = "__all__"
        
    def __init__ (self,*args,**kwargs): # args/kwargs - mogu se koristitit za više vrijednosti u funkciji, rječnike, prosljeđivanje
        super(CarForms,self).__init__(*args,**kwargs) # primjer nasljeđivanja
        #upravljanje poljima. U polju brand_id su bile crtice, sada će pisati select
        self.fields["brand_id"].empty_label = "select"
        self.fields["name"] = forms.CharField(label = "Car name and model.    (Example. Mazda cx5)",widget=forms.TextInput(attrs={"placeholder":"Car"}))
        self.fields["fuel"] = forms.CharField(label = "Diesel/Gasoline",widget=forms.TextInput(attrs ={"placeholder" : "Fuel"}))
        self.fields["brand_id"].label = "Brand"

    
