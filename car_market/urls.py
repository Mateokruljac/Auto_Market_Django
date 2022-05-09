from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name ="base"),
    path('create',views.create,name="create"),
    path('see_all',views.see_all,name = "see_all"),
    path('/delete/<int:car_id>',views.delete,name = "delete"),
    path('update/<int:car_id>',views.update)
    
] 