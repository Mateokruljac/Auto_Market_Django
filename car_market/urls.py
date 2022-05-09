from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name ="base"),
    path('create',views.create,name="create"),
    path('see_all',views.see_all,name = "see_all"),
    path('<int:id>',views.delete,name = "delete"),
    path('<int:id>',views.update_car, name = "update"),
    
] 