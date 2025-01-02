from django.shortcuts import render,redirect
from AdminApp.models import *
from UserApp.models import *
from Employee.models import *

# Create your views here.
def home_page(request):
    detail=Job.objects.all()
    details=Eregister.objects.all()
    context={
        'detail':detail,
        'details':details
    }
    return render(request,'home_page.html',context)


def employees(request):
    details=Eregister.objects.filter(status=1)
    context={
        'details':details
    }
    return render(request,'employees.html',context)

def jobs(request):
    details=Job.objects.all()
    context={
        'details':details
    }
    return render(request,'jobs.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# def filter_services(request,category_name):
#     details=Service.objects.filter(category=category_name)
#     context={
#         'details':details
#     }
#     return render(request,'filter_services.html',context)

def single(request,id):
    detail=Job.objects.filter(id=id)
    context={
        'detail':detail
    }
    return render(request,'single.html',context)

def singleemp(request,id):
    detail=Eregister.objects.filter(id=id)
    context={
        'detail':detail
    }
    return render(request,'singleemp.html',context)

def contact_data(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        message=request.POST['messages']
        result=Contact(firstname=firstname,lastname=lastname,email=email,message=message)
        result.save()
        return redirect('contact')
    
def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def register_data(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        number=request.POST['number']
        result=Register(username=username,password=password,email=email,number=number)
        result.save()
        return redirect('login')
    
def login_data(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(username=username,password=password).exists():
           data = Register.objects.filter(username=username,password=password).values('id','number','email').first()
           request.session['number_u'] = data['number'] 
           request.session['u_id'] = data['id'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('home_page') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')
    
def userlogout(request):
    del request.session['u_id']
    del request.session['number_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

def booking(request,id):
    data=Job.objects.filter(id=id)
    return render(request,'booking.html',{'data':data})

def bookingdata(request,id):
    if request.method == 'POST':
        uid=request.session.get('u_id')
        resume=request.FILES['resume']
        cvletter=request.POST['cvletter']
        data=Booking(uid=Register.objects.get(id=uid),jid=Job.objects.get(id=id),resume=resume,coverletter=cvletter)
        data.save()
    return redirect('status')

def empbooking(request,id):
    data=Eregister.objects.filter(id=id)
    data1=Job.objects.all()
    return render(request,'empbooking.html',{'data':data,'data1':data1})

def empbookingdata(request,id):
    if request.method == 'POST':
        uid=request.session.get('u_id')
        job=request.POST.get('job')
        resume=request.FILES['resume']
        cvletter=request.POST['cvletter']
        data=Ebooking(uid=Register.objects.get(id=uid),eid=Eregister.objects.get(id=id),resume=resume,job=job,coverletter=cvletter)
        data.save()
    return redirect('empbooking',id)

def status(request):
    uid=request.session.get('u_id')
    data=Booking.objects.filter(uid=uid)
    return render(request,'status.html',{'data':data})




