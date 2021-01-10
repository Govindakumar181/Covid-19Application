from django.db import models

# Create your models here.
class world(models.Model):
    sno = models.AutoField(primary_key=True)
    total_cases = models.CharField(max_length=5000)
    total_deaths = models.CharField(max_length=5000)
    active_cases = models.CharField(max_length=5000)
    recovered = models.CharField(max_length=5000)
    timeStamp = models.DateTimeField(blank=True)
    # thumbnail = models.ImageField(upload_to='blog/images', default="")
    # image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return "Name is:- "+self.total_cases

class pakistan(models.Model):
    sno = models.AutoField(primary_key=True)
    total_cases = models.CharField(max_length=5000)
    total_deaths = models.CharField(max_length=5000)
    active_cases = models.CharField(max_length=5000)
    recovered = models.CharField(max_length=5000)
    timeStamp = models.DateTimeField(blank=True)
    # thumbnail = models.ImageField(upload_to='blog/images', default="")
    # image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return "Name is:- "+self.total_cases

class pakistan_hospitals(models.Model):
    sno = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images', default="")
    hospital_name = models.CharField(max_length=5000)
    hospital_address = models.CharField(max_length=5000)
    total_beds = models.CharField(max_length=5000)
    remaining_beds = models.CharField(max_length=5000)
    timeStamp = models.DateTimeField(blank=True)
    # thumbnail = models.ImageField(upload_to='blog/images', default="")
    # image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return "Name is:- "+self.hospital_name+" , Address is:- "+self.hospital_address