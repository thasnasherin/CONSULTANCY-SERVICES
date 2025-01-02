from django.db import models
from AdminApp.models import*
from Employee.models import*
# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

class Register(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField()    

class  Booking(models.Model):
    uid=models.ForeignKey(Register,on_delete=models.CASCADE)
    jid=models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    resume=models.FileField(upload_to='resumes')
    coverletter=models.CharField(max_length=500)
    status=models.IntegerField(default=0)

class  Ebooking(models.Model):
    uid=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    eid=models.ForeignKey(Eregister,on_delete=models.CASCADE,null=True)
    job=models.CharField(max_length=20,default='')
    resume=models.FileField(upload_to='resumes')
    coverletter=models.CharField(max_length=500)
    status=models.IntegerField(default=0)
