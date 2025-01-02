from django.urls import path
from . import views

urlpatterns = [
    path('hrindex',views.hrindex,name='hrindex'),

]