from django import forms
from .models import Car
class CarForms (forms.ModelForm):
    # mijenja način rada ili ponašanje, opcije...
    class Meta: # inner klasa kojom dodjeljujemo metapodatak -> odnosno sve što nije polje
         
        model = Car # model kojim se bavimo je Car
        fields = "__all__"
        
    def __init__ (self,*args,**kwargs): # args/kwargs - mogu se koristitit za više vrijednosti u funkciji, rječnike, prosljeđivanje
        super(CarForms,self).__init__(*args,**kwargs) # primjer nasljeđivanja
        #upravljanje poljima. U polju brand_id su bile crtice, sada će pisati select
        self.fields["brand_id"].empty_label = "select"
        
        