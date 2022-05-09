from django.shortcuts  import render
from car_market.forms  import CarForms
from django.contrib    import messages
from car_market.models import Car
from django.http       import HttpResponse
# Create your views here.

# potrebni su nam pogledi: (lista, koja će biti dostupna u svim mogućnostima), kreiranje, modificiranje, brisnje
def base (requests):
    return render (requests,"base.html") # osnovna stranica 

def see_all (requests):
    # ostvaruje se pristup svim automobilima u bazi podataka
    if requests.method == "GET": 
     car_list = Car.objects.all()# svi automobili
     # vraća na stranicu see_all i na mjestu car_list vraća popis automobila    
     return render (requests,"see_all.html",{"car_list" : car_list })

def create (requests):
    # nakon što smo kreirali CarForms moramo ga i uvrstiti među poglede kako bismo mogli s njim raditi 
    if requests.method == "GET":
        form  = CarForms()
        return render(requests,"create.html",{"form":form})
    else:
        # potrebno je kreirati instancu carForms i popuniti podacima iz zahtjeva
        form = CarForms(requests.POST)
        # potrebno je provjeriti je li zahtjev ispravan, ako je sačuvati ga i ispisati poruku da zna i korisnik da je sve uspješno
        if form.is_valid():
            form.save();
            messages.info(requests,"New car successfully created!")
            return render(requests,"base.html")  #vraća na osnovnu stranicu 
        else:
            return HttpResponse("<h3> Something went wrong </h3>") 
        


def update_car (requests,id=0): # id nam je potreban da odredimo koji točno automobil želimo nadograditi
 # ako je zahtjev GET tj. ako povlačimo podatke
 if requests.method == "GET":
        if id == 0:
            form = CarForms()
        else:
            car = Car.objects.get(pk=id)
            form = CarForms(instance=car)
        return render(requests, "create.html", {'form': form})
 # ako je zahtjev post, tj unosimo podatke
 else:
        if id == 0:
            form = CarForms(requests.POST) # prima post
        else:
            selected_car = Car.objects.get(pk=id) # biramo automobil na temelju id
            form = CarForms(requests.POST,instance= selected_car)
        #potrebno je provjeriti je li ispravno i aoko je sačuvati, te vratiti na glavnu stranicu
        if form.is_valid():
            form.save();
        return render(requests,'base.html')


def delete(requests,id):
    #potrebno je izabrati id autombila kojeg želimo izbrisati
    # u slučaju da automobil ne postoji izbacit će errror. Da se to ne bi dogodilo vratit ćemo ga na glavnu stranicu
    try:
        select_car = Car.objects.get(id = id)
    except Car.DoesNotExist:
        return render (requests,"base.html")
    #ako je sve uspješno automobil će biti izbrisan, te ćemo korisnika vratiti na glavni izbor kako bi se odlučio za sljedeću radnju
    select_car.delete();
    return render (requests,"base.html")



