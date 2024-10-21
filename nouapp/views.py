from django.shortcuts import render,redirect,reverse
from .models import Enquiry, Login, Student
from datetime import date
from django.contrib import messages
from adminapp.models import Program,Branch,Year,News
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from . import smssender
# Create your views here.
def index(request):
    ns=News.objects.all()
    return render(request,'index.html',locals())

def aboutus(request):
    ns=News.objects.all()
    return render(request,'aboutus.html',locals())
def about2 (request):
    ns=News.objects.all()
    return render(request,'about2.html',locals())
def about3 (request):
    return render(request,'about3.html')
def about4 (request):
    return render(request,'about4.html')
def about5 (request):
    return render(request,'about5.html')


def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        usertype='Student'
        status='false'
        regdate=date.today()
        reg=Student(rollno=rollno, name=name, address=address, fname=fname, mname=mname, gender=gender, program=program, branch=branch, year=year, contactno=contactno, emailaddress=emailaddress, regdate=regdate,)
        log=Login(userid=rollno, password=password,usertype=usertype,status=status)
        reg.save()
        log.save()
        
        messages.success(request,'Registration Completed')
        msg=f' Welcome {name},your registration successfull. Your userid is {rollno}, Your passwrd is {password}, You mobile no is {contactno}, registration date is {regdate},Thanks for e-gyane uon portal registration..'
        subj='Registration successfull'        
        from_mail='mailmsg50@gmail.com'
        seen=EmailMultiAlternatives(subj,msg,from_mail,[emailaddress])
        seen.send()
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    ns=News.objects.all()   
    return render(request,'registration.html',locals())


def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid, password=password)
            if obj.usertype=="Student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
                
        except:
            messages.success(request,'Invalid User')
    ns=News.objects.all()        
    return render(request,'login.html',locals())
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name, gender=gender, address=address,contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext, enquirydate=enquirydate )
        enq.save()
        # smssender.sendsms(contactno)
        messages.success(request,'Enquiry is submitted')
    ns=News.objects.all()    
    return render(request,'contactus.html',locals())
def forgotpass(request):
    if request.method == "POST":
        userid=request.POST['userid']
        usertype=request.POST['emailid']
        try:
            data=Login.objects.get(userid=userid)
            if data.userid==userid:
            
                messages.success(f'password {{data.password}}')
            else:
                messages.success(request,'invalide user id')
        except:
            messages.success(request,'invalide') 
    return render(request,'forgotpass.html')