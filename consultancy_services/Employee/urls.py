from django.urls import path
from . import views

urlpatterns = [
   path('empindex',views.empindex,name='empindex'),
   path('emplogin',views.emplogin,name='emplogin'),
   path('empreg',views.empreg,name='empreg'),
   path('empregdata',views.empregdata,name='empregdata'),
   path('emplogdata',views.emplogdata,name='emplogdata'),
   path('emplogout',views.emplogout,name='emplogout'),
   path('clientreq',views.clientreq,name='clientreq'),
   path('jobdetails',views.jobdetails,name='jobdetails'),




]