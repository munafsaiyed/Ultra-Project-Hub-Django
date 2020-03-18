from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
import csv
import io
import datetime
from django.core.mail import send_mail
from django.conf import settings
import os
from django.http import FileResponse
from reportlab.pdfgen import canvas

def indexfunction(request):
    if request.session.has_key('username'):
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def contactfunction(request):
    return render(request,'contact.html')

def teamfunction(request):
    return render(request,'team.html')

def cregistration_form(request):
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    conpass = request.POST["conpass"]
    if(password == conpass):
        regis =Registration_client(full_name=full_name,email=email,password=password)
        regis.save()
        print("Query Inserted...")
    else:
        print("password and confirmed password")
    return render(request,'index.html')
def dregistration_form(request):
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    conpass = request.POST["conpass"]
    if(password == conpass):
        regis =Registration_developer(full_name=full_name,email=email,password=password)
        regis.save()
        print("Query Inserted...")
    else:
        print("password and confirmed password")
    return render(request,'index.html')


def update_form(request):
    email = request.POST["email"]
    updateq = Registration.objects.get(email=email)
    updateq.full_name = request.POST["fullname"]
    updateq.password = request.POST["password"]
    updateq.username = request.POST["username"]
    updateq.contact = request.POST["contact"]
    updateq.addresh = request.POST["addresh"]
    updateq.city = request.POST["city"]
    updateq.country = request.POST["country"]
    updateq.pincode = request.POST["pincode"]
    updateq.email = email
    updateq.save()  
    return HttpResponseRedirect('/admin_user/')
def loginc(request):
    email = request.POST["email"]
    login_pass = request.POST["login_pass"]
    login_obj = Registration_client.objects.filter(email=email,password=login_pass).exists()
    log = Registration_client.objects.get(email=email,password=login_pass)
    if login_obj:  
        request.session['username']=log.cid
        return HttpResponseRedirect('/cliindex/')
    else:
        return HttpResponseRedirect('/index/')
def logindev(request):
    email = request.POST["email"]
    login_pass = request.POST["login_pass"]
    login_obj = Registration_developer.objects.filter(email=email,password=login_pass).exists()
    log = Registration_developer.objects.get(email=email,password=login_pass)
    if login_obj:  
        request.session['username']=log.Did
        return HttpResponseRedirect('/dev_dashboard/')
    else:
        return HttpResponseRedirect('/index/')
def contact_form(request):
    name = request.POST["Name"]
    email = request.POST["Email"]
    phone = request.POST["Phone"]
    message = request.POST["Message"]
    form_entry = Contact_form(name=name,email=email,phone=phone,message=message)
    form_entry.save()
    return render(request,'index.html')
#logout
def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect('/index/')
def project(request):
    if request.session.has_key('username'):
        return render(request,'project.html')
    else:
        return HttpResponseRedirect('/index/')
#def admin_user(request):
#    read=Registration.objects.get(email="saiyedmunaf110@gmail.com")
#    return render(request,'admin/user.html',{'read':read})
#def admin_registration(request):
#    regisq = Registration.objects.all()
#    return render(request,'admin/registration.html',{'regisq':regisq})
#def admin_reg_del(request,email):
#    email=format(email)
#    regdel = Registration.objects.get(email=email)
#    regdel.delete()
#    return HttpResponseRedirect('/admin_registration/')
#def admin_usr_detail(request,email):
#    email=format(email)
#    read = Registration.objects.get(email=email)
#    return render(request,'admin/user.html',{'read':read})
#def dashboard(request):
#    return render(request,'dashboard.html')
#def admin_bid(request):

#    return render(request,'admin/bid.html')
#def admin_query(request):
#    cont = Contact_form.objects.all()
#    return render(request,'admin/query.html',{'cont':cont})

#def fileform(request):
#    return render(request,'filedemo.html')

#file upload
#def app_save(request):
#    if request.method == 'POST':
#        newdoc = Document(doc_file=request.FILES.get('myfile'))
#        newdoc.save()
#    return HttpResponseRedirect('/index/')
#def admin_project(request):
#    proq=Project.objects.all()
#    return render(request,'admin/project.html',{'proq':proq})

#2ADMIN
#def admin_index(request):
#    return render(request,'admin/index.html')
#def admin_index2(request):
#    return render(request,'admin/index2.html')
#def admin_index3(request):
#    return render(request,'admin/index3.html')
#def admin_badge(request):
#    return render(request,'admin/badge.html')
#def admin_alert(request):
#    return render(request,'admin/alert.html')
#def admin_card(request):
#    return render(request,'admin/card.html')
#def admin_chart(request):
#    return render(request,'admin/chart.html')
#def admin_font(request):
#    return render(request,'admin/fontawesome.html')
def dev_fp(request):
    return render(request,'admin/forget-pass-d.html')
def cli_fp(request):
    return render(request,'admin/forget-pass-c.html')
#def admin_form(request):
#    return render(request,'admin/form.html')
#def admin_grid(request):
#    return render(request,'admin/grid.html')
#def admin_inbox(request):
#    return render(request,'admin/inbox.html')
#def admin_index4(request):
#    return render(request,'admin/index4.html')
#def admin_login(request):
#    return render(request,'admin/login.html')
#def admin_map(request):
#    return render(request,'admin/map.html')
#def admin_modal(request):
#    return render(request,'admin/modal.html')
#def admin_probar(request):
#    return render(request,'admin/progress-bar.html')
#def admin_register(request):
#    return render(request,'admin/register.html')
#def admin_switch(request):
#    return render(request,'admin/switch.html')
#def admin_tab(request):
#    return render(request,'admin/tab.html')
#def admin_table(request):
#    return render(request,'admin/table.html')
#def admin_typo(request):
#    return render(request,'admin/typo.html')


#main_admin
def admin_cf(request):
    if request.session.has_key('username'):
        conform = Contact_form.objects.all()
        return render(request,'admin/contactform.html',{'conform':conform})
    else:
        return HttpResponseRedirect('/admin_login/')
def admin_regclient(request):
    if request.session.has_key('username'):
        clientreg = Registration_client.objects.all()
        return render(request,'admin/reg_client.html',{'clientreg':clientreg})
    else:
        return HttpResponseRedirect('/admin_login/')
def admin_clientupdate(request,email):
    if request.session.has_key('username'):
        clread = Registration_client.objects.get(email=email)
        return render(request,'admin/clientupdate.html',{'clread':clread})
    else:
        return HttpResponseRedirect('/admin_login/')
def admin_clientupdatein(request):
    if request.session.has_key('username'):
        profile_pic = request.FILES.get('profile')
        email = request.POST["email"]
        clin = Registration_client.objects.get(email=email)
        clin.username = request.POST["username"]
        clin.gender = request.POST["gender"]
        clin.email = email
        clin.dob = request.POST["dob"]
        clin.contact = request.POST["contact"]
        clin.password = request.POST["password"]
        clin.full_name = request.POST["fullname"]
        clin.addresh = request.POST["addresh"]
        clin.city = request.POST["city"]
        clin.country = request.POST["country"]
        clin.pincode = request.POST["pincode"]
        clin.profile_pic = profile_pic
        clin.save()
        
        return HttpResponseRedirect('/admin_regclient/')
    else:
        return HttpResponseRedirect('/admin_login/')
def admin_clientdel(request,email):
    if request.session.has_key('username'):
        clidel = Registration_client.objects.get(email=email)
        clidel.delete()
        return HttpResponseRedirect('/admin_regclient/')
    else:
        return HttpResponseRedirect('/admin_login/')

#Admin Dashboard render
def admin_indexm(request):
    if request.session.has_key('username'):
        client = Registration_client.objects.all().count()
        dev = Registration_developer.objects.all().count()
        return render(request,'admin/admin_index.html',{'client':client,'dev':dev})
    else:
        return HttpResponseRedirect('/admin_login/')

#View Developer Registeration records in table
def admin_developer(request):
    if request.session.has_key('username'):
        devquery = Registration_developer.objects.all()
        return  render(request,'admin/reg_developer.html',{'devquery':devquery})
    else:
        return HttpResponseRedirect('/admin_login/')

#Render Developer update form with passing values
def admin_developerupdate(request,email):
    if request.session.has_key('username'):
        devuquery = Registration_developer.objects.get(email=email)
        return  render(request,'admin/developerupdate.html',{'devuquery':devuquery})
    else:
        return HttpResponseRedirect('/admin_login/')

#Update developer records
def admin_developerupdatein(request):
    if request.session.has_key('username'):
        email = request.POST["email"]
        profile_pic = request.FILES.get('profile')
        clin = Registration_developer.objects.get(email=email)
        clin.Dname = request.POST["username"]
        clin.gender = request.POST["gender"]
        clin.email = email
        clin.dob = request.POST["dob"]
        clin.contact = request.POST["contact"]
        clin.password = request.POST["password"]
        clin.full_name = request.POST["fullname"]
        clin.addresh = request.POST["addresh"]
        clin.city = request.POST["city"]
        clin.country = request.POST["country"]
        clin.pincode = request.POST["pincode"]
        clin.skill = request.POST["skill"]
        clin.experience = request.POST["experience"]
        clin.profile_pic = profile_pic
        clin.save()
        return HttpResponseRedirect('/admin_developer/')
    else:
        return HttpResponseRedirect('/admin_login/')

#Delete Developer Row
def admin_developerdel(request,email):
    if request.session.has_key('username'):
        devdel = Registration_developer.objects.get(email=email)
        devdel.delete()
        return HttpResponseRedirect('/admin_developer/')
    else:
        return HttpResponseRedirect('/admin_login/')

#admin login page render
def admin_login(request):
    return render(request,'admin/login.html')

#admin login Check
def admin_loginauth(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        admincheck = Admin.objects.get(email=email,password=password)
        if admincheck.email==email and admincheck.password==password:
            request.session["username"]=email
            return HttpResponseRedirect('/admin_indexm/')
        else:
            return HttpResponseRedirect('/admin_login/')
    except:
        return HttpResponseRedirect('/admin_login/')

#for Logout
def admin_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect('/admin_login/')

# For Exporting Client Registration Records
#def export_users_csv(request):
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="users.csv"'
#    
#    writer = csv.writer(response)
#    writer.writerow(['ID','Username', 'Profile', 'Gender', 'DOB', 'Email', 'Contact', 'Password', 'Full Name', 'Addresh', 'City','Country','Pincode'])

#    users = Registration_client.objects.all().values_list('cid','username', 'profile_pic', 'gender', 'dob', 'email', 'contact', 'password', 'full_name', 'addresh', 'city','country','pincode')
#    for user in users:  
#        writer.writerow(user)
#    return response

# For Exporting Developer Registration Records    
#def export_dev_csv(request):
#    response = HttpResponse(content_type='text/csv')
#    response['Content-Disposition'] = 'attachment; filename="users.csv"'
#    
#    writer = csv.writer(response)
#    writer.writerow(['ID','Username', 'Profile', 'Gender', 'DOB', 'Email', 'Contact', 'Password', 'Full Name', 'Addresh', 'City','Country','Pincode', 'Skill', 'Experience'])

#    users = Registration_developer.objects.all().values_list('cid','username', 'profile_pic', 'gender', 'dob', 'email', 'contact', 'password', 'full_name', 'addresh', 'city','country','pincode', 'skill', 'experience')
#    for user in users:  
#        writer.writerow(user)
#    return response

#Client Bulk data import with csv file   
def importcsvc(request):
    if request.session.has_key('username'):
        csv_file = request.FILES.get('importfile')
        csvfile = request.FILES['importfile']
        csvquery = importcsv(csvfile=csv_file)
        csvquery.save()
        dataset = csvfile.read().decode('UTF-8')
        io_string =io.StringIO(dataset)
        reader = csv.reader(io_string, delimiter=',', quotechar="|")
        next(reader)
        print(reader)
        for column in reader:
            bulkrecord = Registration_client(
                username=column[0],
                gender=column[2],
                dob=column[3],
                email=column[4],
                contact=column[5],
                password=column[6],
                full_name=column[7],
                addresh=column[8],
                city=column[9],
                country=column[10],
                pincode=column[11],

            )
            bulkrecord.save()
            print(bulkrecord)
            
        return  HttpResponseRedirect('/admin_regclient/')
    else:
        return HttpResponseRedirect('/admin_login/')

#Developer Bulk data import with csv file   
def importcsvd(request):
    if request.session.has_key('username'):
        csvfile = request.FILES['importfile']
        dataset = csvfile.read().decode('UTF-8')
        io_string =io.StringIO(dataset)
        reader = csv.reader(io_string, delimiter=',', quotechar="|")
        next(reader)
        print(reader)
        for column in reader:
            bulkrecord = Registration_developer(
                Dname=column[0],
                gender=column[2],
                dob=column[3],
                email=column[4],
                contact=column[5],
                password=column[6],
                full_name=column[7],
                addresh=column[8],
                city=column[9],
                country=column[10],
                pincode=column[11],
                skill=column[12],
                experience=column[13]

            )
            bulkrecord.save()
            print(bulkrecord)
            
        return  HttpResponseRedirect('/admin_regclient/')
    else:
        return HttpResponseRedirect('/admin_login/')

#For rendering admin project table entries
def reg_project(request):
    if request.session.has_key('username'):
        proj = Project.objects.prefetch_related('cid')
        return render(request,'admin/reg_project.html',{'proj':proj})
    else:
        return HttpResponseRedirect('/admin_login/')
#for insert client project
def projectin(request):
    if request.session.has_key('username'):
        pname = request.POST["projectname"]
        pdesc = request.POST["projectdesc"]
        pfile = request.FILES.get('pfile')
        pskill = request.POST["skill"]
        ptype = request.POST["projtype"]
        if request.POST["currencypro"]:
            curr = request.POST["currencypro"]
        elif request.POST["currencyhr"]:
            curr = request.POST["currencyhr"]
    
        if request.POST["pricepro"]:
            if request.POST["pricepro"] == 'custompro':
                minprice = request.POST["minpro"]
                maxprice = request.POST["maxpro"]
            else:
                minprice, maxprice = request.POST["pricepro"].split('-')
        elif request.POST["pricehr"]:
            if request.POST["pricehr"] == 'customhr':
                minprice = request.POST["minhr"]
                maxprice = request.POST["maxhr"]
            else:
                minprice, maxprice = request.POST["pricehr"].split('-')
        proquery = Project(projname=pname,projdesc=pdesc,projpaytype=ptype,curr=curr,maxprice=maxprice,minprice=minprice,projfile=pfile,projskills=pskill)
        proquery.save()
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/admin_login/')
# For Download project data files    
def export_project(request,id):
    if request.session.has_key('username'):
        file_name = Project.objects.get(pid=id).projfile
        ext = file_name.name.split('.')[1].lower()
        file_path = os.path.join(settings.MEDIA_ROOT, file_name.url)
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="Projectdata.%s"' % ext
        return response
    else:
        return HttpResponseRedirect('/admin_login/')

#for rendering admin bid page
def bidding(request,id):
    if request.session.has_key('username'):
        qbid = bid.objects.prefetch_related('Did').filter(pid=id).order_by('date_time')
        return render(request,'admin/bid.html',{'qbid':qbid})
    else:
        return HttpResponseRedirect('/admin_login/')
#confirming project bid by admin
def bid_confirm(request,id):
    if request.session.has_key('username'):
        pid = bid.objects.get(id=id)
        pid.status = "Approved"
        pid.save()
        query = bid.objects.filter(pid_id=pid.pid_id).exclude(id=id)
        for q in query:
            q.status = "Cancelled"
            q.save()
        noti = noti_developer(sender_id_id=1,recev_id_id=pid.Did_id,message="Bidding on the project has been Approved Congrats",date_time=datetime.datetime.now())
        noti.save()
        return HttpResponseRedirect('/reg_project/')
    else:
        return HttpResponseRedirect('/admin_login/')
#Project Admin Delete
def projdel(reguest,id):
    if request.session.has_key('username'):
        prodel = Project.objects.get(pid=id)
        prodel.delete()
        return HttpResponseRedirect('/reg_project/')
    else:
        return HttpResponseRedirect('/admin_login/')
def resetdone(request):
    return render(request,'forget/password_reset_done.html')
def resetconfirm(request):
    return render(request,'forget/password_reset_confirm.html')
def resetcomplete(request):
    return render(request,'forget/password_reset_complete.html')
def resetpassword(request,id):
    return render(request,'forget/passwordreset.html',{'id':id})
def resetpasswordc(request,id):
    return render(request,'forget/passwordresetc.html',{'id':id})
    #forgot Password Link render
def smail(request):
    pemail = request.POST["email"]
    try:
        cmail = Registration_developer.objects.get(email=pemail)
        #print(cmail)
        if(cmail.email==pemail):
            subject = 'Forget Password for UPH'
            message = 'Click On link To Reset Your Password \n\n\n\n http://localhost:8000/resetpassword/%s/' % cmail.Did
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [cmail.email,]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect('/resetdone/')
        else:
            return HttpResponseRedirect('/dev_fp/')
    except:
        return HttpResponseRedirect('/dev_fp/')
    #forgot Password Link render for client
def smailc(request):
    pemail = request.POST["email"]
    try:
        cmail = Registration_client.objects.get(email=pemail)
        #print(cmail)
        if(cmail.email==pemail):
            subject = 'Forget Password for UPH'
            message = 'Click On link To Reset Your Password \n\n\n\n http://localhost:8000/resetpasswordc/%s/' % cmail.cid
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [cmail.email,]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponseRedirect('/resetdone/')
        else:
            return HttpResponseRedirect('/cli_fp/')
    except:
        return HttpResponseRedirect('/cli_fp/')

#insert forget pass in database
def upresetpass(request,id):
    aid=id
    password = request.POST["password"]
    cpassword = request.POST["cpassword"]
    if(password == cpassword):
        try:
            query = Registration_developer.objects.get(Did=aid)
            query.password = password
            query.save()
            return HttpResponseRedirect('/resetcomplete/')
        except:
            return HttpResponseRedirect('/resetconfirm/')
    else:
        return HttpResponseRedirect('/resetconfirm/')
#insert forget pass in database client
def upresetpassc(request,id):
    aid=id
    password = request.POST["password"]
    cpassword = request.POST["cpassword"]
    if(password == cpassword):
        try:
            query = Registration_client.objects.get(cid=aid)
            query.password = password
            query.save()
            return HttpResponseRedirect('/resetcomplete/')
        except:
            return HttpResponseRedirect('/resetconfirm/')
    else:
        return HttpResponseRedirect('/resetconfirm/')
#Developer Panel
#dashboard
def dev_project(request):
    if request.session.has_key('username'):
        d=request.session["username"]
        dev=Registration_developer.objects.get(Did=d)
        tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did)
        noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
        #bid.objects.prefetch_related('Did').filter(pid=id)
        return render(request,'developer/table.html',{'tbl':tbl,'dev':dev,'noti':noti})
    else:
        return HttpResponseRedirect('/index/')
#confirm Project
def dev_confirm(request):
    if request.session.has_key('username'):
        d=request.session["username"]
        dev=Registration_developer.objects.get(Did=d)
        tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did,status="Approved")
        noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
        #bid.objects.prefetch_related('Did').filter(pid=id)
        return render(request,'developer/confirmproj.html',{'tbl':tbl,'dev':dev,'noti':noti})
    else:
        return HttpResponseRedirect('/index/')

def popupupload(request,id):
    if request.session.has_key('username'):
        d=request.session["username"]
        dev=Registration_developer.objects.get(Did=d)
        tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did,status="Approved")
        noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
        #bid.objects.prefetch_related('Did').filter(pid=id)
        return render(request,'developer/confirmproj.html',{'id':id,'tbl':tbl,'dev':dev,'noti':noti})
    else:
        return HttpResponseRedirect('/index/')

def upprojfile(request,id):
    if request.session.has_key('username'):
        d=request.session["username"]
        upfile = projectfile(pid_id=id,did_id=d,pfile=request.FILES.get('file'))
        upfile.save()
        dev=Registration_developer.objects.get(Did=d)
        tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did,status="Approved")
        noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
        return render(request,'developer/confirmproj.html',{'tbl':tbl,'dev':dev,'noti':noti})
    else:
        return HttpResponseRedirect('/index/')


def dev_inbox(request):
    return render(request,'developer/inbox.html')
def dev_form(request):
    if request.session.has_key('username'):
        d=request.session["username"]
        #did=Registration_developer.objects.get(Did=d).Did
        dev=Registration_developer.objects.get(Did=d)
        devread=Registration_developer.objects.get(Did=d)
        noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
    
        return render(request,'developer/form.html',{'devread':devread,'dev':dev,'noti':noti})
def cli_form(request):
    if request.session.has_key('username'):
        d=request.session["username"]
        dev=Registration_client.objects.get(cid=d)
        devread=Registration_client.objects.get(cid=d)
        return render(request,'client/form.html',{'devread':devread,'dev':dev})

def dev_profileupdate(request):
    email = request.POST["email"]
    devupdate = Registration_developer.objects.get(email=email)
    devupdate.full_name = request.POST["fullname"]
    devupdate.password = request.POST["password"]
    #devupdate.username = request.POST["username"]
    devupdate.contact = request.POST["contact"]
    devupdate.address = request.POST["address"]
    devupdate.city = request.POST["city"]
    devupdate.country = request.POST["country"]
    devupdate.pincode = request.POST["pincode"]
    devupdate.email = email
    devupdate.skill = request.POST["skill"]
    devupdate.experience = request.POST["experience"] 
    devupdate.profile = request.FILES["profile"]
    devupdate.save()  
    return HttpResponseRedirect('/devindex/')
def cli_profileupdate(request):
    email = request.POST["email"]
    devupdate = Registration_client.objects.get(email=email)
    devupdate.full_name = request.POST["fullname"]
    devupdate.password = request.POST["password"]
    #devupdate.username = request.POST["username"]
    devupdate.contact = request.POST["contact"]
    devupdate.addresh = request.POST["address"]
    devupdate.city = request.POST["city"]
    devupdate.country = request.POST["country"]
    devupdate.pincode = request.POST["pincode"]
    devupdate.email = email
    devupdate.profile = request.FILES["profile"]
    devupdate.save()  
    return HttpResponseRedirect('/cliindex/')

def devindex(request):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    proj = Project.objects.all()
    noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
    return render(request,'developer/index.html',{'dev':dev,'proj':proj,'noti':noti})
def bidpopup(request,id):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    proj = Project.objects.all()
    if request.method == 'POST':
        price = request.POST["price"]
        days = request.POST["days"]
        #did = request.session["username"]
        query = bid(Did_id=dev.Did,pid_id=id,price=price,days=days,date_time=datetime.datetime.now())
        query.save()
        print(datetime.datetime.now())
        return HttpResponseRedirect('/devindex/')
    else:
        return render(request,'developer/index.html',{'id':id,'dev':dev,'proj':proj})
def dev_dashboard(request):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    proj = Project.objects.all()
    noti = noti_developer.objects.filter(recev_id_id=dev.Did).order_by('-date_time')[0:5]
    return render(request,'developer/index2.html',{'dev':dev,'proj':proj,'noti':noti})
def cli_dashboard(request):
    cid=request.session["username"]
    dev = Registration_client.objects.get(cid=cid)
    proj = Project.objects.filter(cid_id=cid)
    noti = noti_developer.objects.filter(recev_id_id=dev.cid).order_by('-date_time')[0:5]
    return render(request,'client/index2.html',{'dev':dev,'proj':proj,'noti':noti})

def descpopup(request,id):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    proj = Project.objects.all()
    desc = Project.objects.get(pid=id)
    return render(request,'developer/index.html',{'desc':desc,'dev':dev,'proj':proj})
def descpopupd(request,id):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did,status="Approved")
    desc = Project.objects.get(pid=id)
    return render(request,'developer/confirmproj.html',{'desc':desc,'dev':dev,'tbl':tbl})

def descpopupcli(request,id):
    did=request.session["username"]
    dev = Registration_developer.objects.get(Did=did)
    tbl=bid.objects.prefetch_related('pid').filter(Did_id=dev.Did,status="Approved")
    desc = Project.objects.prefetch_related('cid').get(pid=id)
    return render(request,'developer/confirmproj.html',{'desc':desc,'dev':dev,'tbl':tbl})
def cdescpopup(request,id):
    did=request.session["username"]
    dev = Registration_client.objects.get(cid=did)
    proj = Project.objects.filter(cid_id=did)
    desc = Project.objects.get(pid=id)
    return render(request,'client/index.html',{'desc':desc,'dev':dev,'proj':proj})

def contact1(request):
    return render(request, 'client/index.html')
def cliindex(request):
    cid=request.session["username"]
    dev = Registration_client.objects.get(cid=cid)
    proj = Project.objects.filter(cid_id=cid)
    return render(request,'client/index.html',{'dev':dev,'proj':proj})
def downloadf(request,id):
    if request.session.has_key('username'):
        file_name = projectfile.objects.filter(pid_id=id).order_by('-id')[1]
        ext = file_name.pfile.name.split('.')[1].lower()
        file_path = os.path.join(settings.MEDIA_ROOT, file_name.pfile.url)
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="Projectdata.%s"' % ext
        return response
    else:
        return HttpResponseRedirect('/index/')

def cpassc(request,id):
    return render(request, 'client/cpassword.html',{'id':id})
def cpasscli(request,id):
    npass = request.POST["password"]
    cpass = request.POST["cpassword"]
    query = Registration_client.objects.get(cid=id)
    if query.password == npass:
        query.password = cpass
        query.save()
    return HttpResponseRedirect('/index/')
def cpassd(request,id):
    return render(request, 'developer/cpassword.html',{'id':id})
def cpassdev(request,id):
    npass = request.POST["password"]
    cpass = request.POST["cpassword"]
    query = Registration_developer.objects.get(Did=id)
    if query.password == npass:
        query.password = cpass
        query.save()
        return HttpResponseRedirect('/dev_dashboard/')
    else:
        return HttpResponseRedirect('/cpassd/',id)
