from django.shortcuts import render
from AdminApp.models import*
from UserApp.models import*
from Employee.models import*
# Create your views here.
def hrindex(request):
    job=Job.objects.all().count()
    emp=Eregister.objects.filter(status=1).count()
    reg=Register.objects.all().count()
    appl=Booking.objects.all().count()
    return render(request,'hrindex.html',{'job':job, 'emp':emp, 'reg':reg, 'appl':appl})