from django.shortcuts import render,redirect
from nouapp . models import Student,Login
from django.views.decorators.cache import cache_control
from .models import stuResponse,Question,Answer
from datetime import date
from adminapp.models import Material
from django.contrib import messages
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'studenthome.html',{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
def studentlogout(request):
    try:
        del request.session['rollno']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def response(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
              responsetype=request.POST['responsetype']
              subject=request.POST['subject']
              responsetext=request.POST['responsetext']
              responsedate=date.today()
              rollno=stu.rollno  
              name=stu.name
              branch=stu.branch
              year=stu.year
              contactno=stu.contactno
              emailaddress=stu.emailaddress
              sr=stuResponse(responsetype=responsetype,rollno=rollno,name=name,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,subject=subject,responsetext=responsetext,responsedate=responsedate)
              messages.success(request,'Response is Submited')
              sr.save()
            return render(request,'response.html', {'stu':stu})
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postquestion(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                question=request.POST['question']
                postedby=stu.name
                posteddate=date.today()
                quse=Question( question=question,postedby=postedby,posteddate=posteddate)
                quse.save()
            quse=Question.objects.all()
            return render(request,'postquestion.html',{'stu':stu,'quse':quse})
    except KeyError:
        return redirect('nouapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'postanswer.html',{'stu':stu,'qid':qid})
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def postans(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=request.POST['qid']
            answer=request.POST['answer']
            answerby=stu.name
            answerdate=date.today()
            ans=Answer(answer=answer,qid=qid,answerby=answerby,answerdate=answerdate)
            ans.save()
            return redirect('studentapp:postquestion')
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewanswer(request,qid):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)
            
            return render(request,'viewanswer.html',{'stu':stu,'ans':ans})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepassword(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                conformpassword=request.POST['conformpassword']
                presentpasssword=Login.objects.get(userid=rollno)
                if oldpassword==presentpasssword.password:
                    if oldpassword!=newpassword:
                        if newpassword==conformpassword:
                            Login.objects.filter(userid=rollno).update(password=newpassword)
                            return redirect('studentapp:studentlogout')
                        else:
                            messages.success(request,'new password and conform password must be same')
                    else:
                        messages.warning(request,'plesse not  enter same password')
                else:
                    messages.error(request,'old password in incorect')
            return render(request,'changepassword.html',{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewprofile(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(request,'viewprofile.html',{'stu':stu})
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudymaterial(request):
    try:
        if request.session['rollno']!=None:
            rollno=request.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            mat=Material.objects.filter(program=stu.program,branch=stu.branch,year=stu.year)
            return render(request,'viewstudymaterial.html',locals())
    except KeyError:
        return redirect('nouapp:login')