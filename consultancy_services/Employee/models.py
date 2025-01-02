from django.db import models

# Create your models here.
class Eregister(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=10,default='')
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    design=models.CharField(max_length=100)
    qual=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images',default='null.jpg')
    status=models.IntegerField(default=0)
