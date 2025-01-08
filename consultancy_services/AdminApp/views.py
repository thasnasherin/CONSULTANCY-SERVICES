from django.shortcuts import render,redirect
from AdminApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from UserApp.models import *
# Create your views here.
def admin_ui(request):
    job=Job.objects.all().count()
    emp=Eregister.objects.filter(status=1).count()
    reg=Register.objects.all().count()
    appl=Booking.objects.all().count()
    return render(request,'admin_ui.html',{'job':job, 'emp':emp, 'reg':reg, 'appl':appl})

def add_jobs(request):
    return render(request,'add_jobs.html')

def jobdata(request):
    if request.method=="POST":
        name=request.POST['name']
        image=request.FILES['image']
        vac=request.POST['vacancy']
        skill=request.POST['skill']
        loc=request.POST['loc']
        sal=request.POST['sal']
        exp=request.POST['exp']
        result=Job(name=name,image=image,vacancy=vac,skill=skill,location=loc,exp=exp,sal=sal)
        result.save()
        return redirect('view_jobs')

def view_jobs(request):
    details=Job.objects.all()
    context={
        'details':details
    }
    return render(request,'view_jobs.html',context)

def edit_job(request,id):
    details=Job.objects.filter(id=id)
    context={
        'details':details
    }
    return render(request,'edit_jobs.html',context)

def update(request,id):
    if request.method=="POST":
        name=request.POST['name']
        vac=request.POST['vacancy']
        skill=request.POST['skill']
        loc=request.POST['loc']
        sal=request.POST['sal']
        exp=request.POST['exp']
        try:
            image= request.FILES['image']
            fs = FileSystemStorage()
            file= fs.save(image.name, image)
        except MultiValueDictKeyError:
            file= Job.objects.get(id=id).image
        Job.objects.filter(id=id).update(name=name,image=file,vacancy=vac,skill=skill,location=loc,exp=exp,sal=sal)
        return redirect('view_jobs')
    
def delete(request,id):
    Job.objects.filter(id=id).delete()
    return redirect('view_jobs')

def viewjobrequests(request):
    data=Booking.objects.filter(status=0)
    return render(request, 'viewjobrequests.html',{'data':data})

def approve(request,id):
    Booking.objects.filter(id=id).update(status=1)
    return redirect('viewjobrequests')

def declain(request,id):
    Booking.objects.filter(id=id).update(status=2)
    return redirect('viewjobrequests')

def approvedrequests(request):
    data=Booking.objects.filter(status=1)
    return render(request, 'approvedrequests.html',{'data':data})

def declainrequests(request):
    data=Booking.objects.filter(status=2)
    return render(request, 'declainedrequests.html',{'data':data})   

def emprequests(request):
    data=Eregister.objects.filter(status=0)
    return render(request, 'employeesrequest.html',{'data':data})

def approve1(request,id):
    Eregister.objects.filter(id=id).update(status=1)
    return redirect('emprequests')

def declain1(request,id):
    Eregister.objects.filter(id=id).update(status=2)
    return redirect('emprequests')

def approvedemp(request):
    data=Eregister.objects.filter(status=1)
    return render(request, 'approvedemployees.html',{'data':data})

def declainedemp(request):
    data=Eregister.objects.filter(status=2)
    return render(request, 'declainedemployees.html',{'data':data})   

def reqthroughemp(request):
    data=Ebooking.objects.filter(status=0)
    return render(request, 'reqthroughemp.html',{'data':data})

def approve2(request,id):
    Ebooking.objects.filter(id=id).update(status=1)
    return redirect('apprreqemp')

def declain2(request,id):
    Ebooking.objects.filter(id=id).update(status=2)
    return redirect('declempreq')

def apprreqemp(request):
    data=Ebooking.objects.filter(status=1)
    return render(request, 'apprreqemp.html',{'data':data})

def declempreq(request):
    data=Ebooking.objects.filter(status=2)
    return render(request, 'declempreq.html',{'data':data})   






# def service_input(request):
#     details=category.objects.all()
#     context={
#         'details':details
#     }
#     return render(request,'service_input.html',context)

# def database(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         image=request.FILES['image']
#         description=request.POST['description']
#         category=request.POST['category']
#         result=Service(name=name,image=image,description=description,category=category)
#         result.save()
#         return redirect('service_input')
    
# def view_service(request):
#     details=Service.objects.all()
#     context={
#         'details':details
#     }
#     return render(request,'view_service.html',context)

# def edit_service(request,id):
#     details=Service.objects.filter(id=id)
#     detail=category.objects.all()
#     context={
#         'details':details,
#          'detail':detail
#     }
#     return render(request,'edit_service.html',context)

# def updating(request,id):
#     if request.method=="POST":
#         name=request.POST['name']
#         description=request.POST['description']
#         category=request.POST['category']
#         try:
#             image= request.FILES['image']
#             fs = FileSystemStorage()
#             file= fs.save(image.name, image)
#         except MultiValueDictKeyError:
#             file= Service.objects.get(id=id).image
#         Service.objects.filter(id=id).update(name=name,description=description,category=category,image=file)
#         return redirect('view_service')
    
# def deleting(request,id):
#     Service.objects.filter(id=id).delete()
#     return redirect('view_service')

def feedback(request):
    details=Contact.objects.all()
    context={
        'details':details
    }
    return render(request,'feedback.html',context)

def registered_users(request):
    details=Register.objects.all()
    context={
        'details':details
    }
    return render(request,'registered_users.html',context)