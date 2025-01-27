from django.shortcuts import render,redirect
from.models import*
from UserApp.models import*
from AdminApp.models import*
from Employee.models import*
# Create your views here.
def empindex(request):
    eid=request.session.get('e_id')
    job=Job.objects.all().count()
    emp=Eregister.objects.filter(status=1).count()
    reg=Register.objects.all().count
    clireq=Ebooking.objects.filter(eid=eid).count()
    data=Job.objects.all()

    return render(request,'empindex.html',{'reg':reg,'clireq':clireq,'job':job,'emp':emp,'data':data})

def emplogin(request):
    return render(request,'emplogin.html')

def empreg(request):
    return render(request,'empregister.html')

def empregdata(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        passw=request.POST.get('pass')
        phone=request.POST.get('phone')
        design=request.POST.get('design')
        qual=request.POST.get('qual')
        image=request.FILES['image']
        data=Eregister(name=name, phone=phone, design=design,email=email,qual=qual,password=passw,img=image)
        data.save()
        return redirect('empreg')
    
def emplogdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Eregister.objects.filter(name=username,password=password).exists():
           data = Eregister.objects.filter(name=username,password=password).values('id','phone','email','design','qual').first()
           request.session['e_id'] = data['id']
           request.session['phonenumber_e'] = data['phone'] 
           request.session['email_e'] = data['email'] 
           request.session['design_e'] = data['design'] 
           request.session['qual_e'] = data['qual'] 
           request.session['username_e'] = username
           request.session['password_e'] = password
           return redirect('empindex') 
        else:
            return render(request,'emplogin.html',{'msg':'invalid user credentials'})
    else:
        return redirect('emplogin')

def emplogout(request):
    del request.session['username_e']
    del request.session['phonenumber_e']
    del request.session['email_e']
    del request.session['qual_e']
    del request.session['design_e']
    del request.session['e_id']
    del request.session['password_e']
    return redirect('empindex')

def clientreq(request):
    if 'e_id' in request.session:
       eid=request.session.get('e_id')
       data=Ebooking.objects.filter(eid=eid)
       return render(request,'viewclientrequests.html',{'data':data})
    return render(request,'emplogin.html',{'msg1':'You need to login first to access this page!'})

def jobdetails(request):
    if 'e_id' in request.session:
       data=Job.objects.all()
       return render(request,'jobdetails.html',{'data':data})
    return render(request,'emplogin.html',{'msg1':'You need to login first to access this page!'})
