from django.db import models



class Job(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images',default='null.jpg')
    vacancy=models.IntegerField()
    skill=models.CharField(max_length=500)
    location=models.CharField(max_length=20)
    exp=models.IntegerField()
    sal=models.IntegerField()