from django.db import models

# Create your models here.

class Registration(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField(null=True, blank=True, default=0)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    addresh = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True, default=0)   

class Contact_form(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=500)

class Document(models.Model):
    doc_file = models.FileField(upload_to='app')

class Project(models.Model):
    userid = models.IntegerField()
    projectname = models.CharField(max_length=200)
    projectdesc = models.CharField(max_length=1000)
    projectfile = models.FileField(upload_to='projectfiles')
    skills = models.CharField(max_length=200)
    paymenttype = models.CharField(max_length=100)
    paymentcur = models.CharField(max_length=10)
    pricemin = models.IntegerField()
    pricemax = models.IntegerField()

class Bid(models.Model):
    projectid = models.ForeignKey(Project,on_delete=models.CASCADE)
    developerid = models.IntegerField()
    bidprice = models.IntegerField()
    days = models.IntegerField()


    