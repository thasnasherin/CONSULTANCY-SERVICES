from django.urls import path
from UserApp import views

urlpatterns = [
    path('home_page',views.home_page,name="home_page"),
    path('jobs',views.jobs,name="jobs"),
    path('employees',views.employees,name="employees"),

    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('single/<int:id>',views.single,name="single"),
    path('singleemp/<int:id>',views.singleemp,name="singleemp"),

    path('contact_data',views.contact_data,name="contact_data"),
    path('login',views.login,name="login"),
    path('',views.registration,name="registration"),
    path('register_data',views.register_data,name="register_data"),
    path('login_data',views.login_data,name="login_data"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('booking/<int:id>',views.booking,name="booking"),
    path('empbooking/<int:id>',views.empbooking,name="empbooking"),

    path('bookingdata/<int:id>',views.bookingdata,name="bookingdata"),
    path('empbookingdata/<int:id>',views.empbookingdata,name="empbookingdata"),
    path('status',views.status,name="status"),
    path('emphistory',views.emphistory,name="emphistory"),


]