from django.db import models

# Create your models here.

class Registration_client(models.Model):
    cid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    gender= models.CharField(max_length=200, null=True, blank=True)
    dob=models.DateField(default='2000-01-01', null=True, blank=True)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField(null=True, blank=True, default=0)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    addresh = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True, default=0)
    profile_pic = models.FileField(upload_to='clientdp',null=True, blank=True, default='clientdp/default.jpg')

class Admin(models.Model):
    Aid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
class Document(models.Model):
    doc_file = models.FileField(upload_to='developerdp')
    
class Registration_developer(models.Model):
    Did = models.AutoField(primary_key=True)
    Dname = models.CharField(max_length=200)
    gender= models.CharField(max_length=200, null=True, blank=True)
    dob=models.DateField(default='2000-01-01', null=True, blank=True)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField(null=True, blank=True, default=0)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    addresh = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True, default=0)
    skill = models.CharField(max_length=200)
    experience=models.IntegerField( default=0) 
    profile_pic = models.FileField(upload_to='developerdp',null=True, blank=True, default='developerdp/default.jpg')


class Contact_form(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=500)


class Project(models.Model):
   pid = models.AutoField(primary_key=True)
   cid = models.ForeignKey(Registration_client,on_delete=models.CASCADE)
   projname = models.CharField(max_length = 50)
   projdesc = models.CharField(max_length=1000)
   projfile = models.FileField(upload_to = 'projectfiles')
   projskills = models.CharField(max_length=100)
   projpaytype = models.CharField(max_length=50)
   curr = models.CharField(max_length=20)
   minprice = models.IntegerField()
   maxprice = models.IntegerField()

   class Meta:
     db_table: "ultra_profile"
    
class bid(models.Model):
    id=models.AutoField(primary_key=True)
    Did=models.ForeignKey(Registration_developer,on_delete=models.CASCADE)
    pid=models.ForeignKey(Project,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    days=models.IntegerField(default=0)
    date_time=models.DateTimeField()
    status=models.CharField(max_length=10,default='Pending')

class noti_developer(models.Model):
    noti_id=models.AutoField(primary_key=True)
    sender_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
    recev_id=models.ForeignKey(Registration_developer,on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    date_time=models.DateTimeField()

class projectfile(models.Model):
    pid = models.ForeignKey(Project,on_delete=models.CASCADE)
    did = models.ForeignKey(Registration_developer,on_delete=models.CASCADE)
    pfile = models.FileField(upload_to = 'finalproject')
    

class importcsv(models.Model):
    csvfile = models.FileField(upload_to='importcsv')