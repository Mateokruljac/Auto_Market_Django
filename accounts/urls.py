from django.urls import path # obuhvaća sve što nije prazno, podudaranje s cijelim url putem
from . import views
#mapiranje url adresa

#putem ovih url adresa, ostvaruje se pristup pogledima 
urlpatterns = [
    path("register",views.register,name = "register"), 
    path("login",views.login,name="login"),
    path("logout",views.logout,name ="logout")
    
    ]