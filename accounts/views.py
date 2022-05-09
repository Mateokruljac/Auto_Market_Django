from django.contrib import messages 
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

#kreiramo poglede za login/registraciju/logout sustav
def login (requests):
    if requests.method == "POST":
        username = requests.POST["username"] # vraća nam vrijednost username-a koji korsnik unese
        password = requests.POST["password"]
        #potrebno je i provjeriti je li korsnik autentičan
        user = auth.authenticate(username = username,password = password)
        # bit će none ako upišemo krivi username ili password
        if user is not None:
            auth.login(requests,user)
            return render(requests,"base.html")
        else:
            messages.info(requests,"Invalid username or password!")
            # nakon registracije korisnika se vraća na login
            redirect("login")
    
    return render (requests,"login.html")

def logout (requests):
    auth.logout(requests) 
    return render(requests,"base.html")


def register (requests):
    #korisnik unosi posdatke za registraciju
    if requests.method  == "POST":
       first_name = requests.POST["first_name"]
       last_name = requests.POST["last_name"]
       username = requests.POST["username"]
       password1 = requests.POST["password1"]
       confirm_password = requests.POST["password2"]
       email = requests.POST["email"]
       #svaki sustav za registraciju zahtjeva ponavljanje lozinke pa sam i ja tako odlučio napraviti
       if password1 == confirm_password:
        #filtriranjem provjeravamo postoji li user u bazi podataka, 
        # ako postoji o tome će korisnik biti obavješten i mora izabrati novi emil/username te ga se vraća da ponovno pokuša
        if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
           messages.info(requests,"Username or email already exists!")
           return redirect("register")
        else:    
            #ako ne napravamo create_user neće se pojaviti u bazi podataka
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password1,
                email = email     
            )
            user.save(); #ključno SQL QUERY
            messages.info(requests,"User successfully  created!")
            #nakon kreiranja računa, vrijeme je da se korisnik logira
            return redirect("login")
       else:# ukoliko se lozinke ne podudaraju
           messages.info(requests,"Password not matching!\n")   
           return redirect("register")
    
    else: 
       return render (requests,"register.html")