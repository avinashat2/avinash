from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import ContactUsmodel, ReplyModel
from datetime import datetime
from django.urls import reverse
# Create your views here.

def Index(request):
    return render(request,'index.html')

def Loginhandle(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in Success !')
            return redirect('index')
        messages.error(request,'Somthing went wrong !')
        return redirect('login')
    return render(request,'login.html')


def Logouthandle(request):
    logout(request)
    messages.success(request,'logged out success !')
    return redirect('index')


def ContactUs(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        contactmessage=ContactUsmodel(name=name,email=email,subject=subject,content=content)
        contactmessage.save()
        # print(contactmessage)
        messages.success(request,'We will get back to you with in 24 hours, Thank you')
        return redirect('contactus')
    return render(request,'contactus.html')


def Dashboard(request):
    contacts=ContactUsmodel.objects.all().order_by('-contact_date')
    print(contacts)
    # print(contacts)

    return render(request,'dashboard.html',{'contactusmessages':contacts})


def Replyhandle(request,id):
    if request.method=='POST':
        contactus=id
        email=request.POST.get('email')
        reply=request.POST.get('reply')
        # print(reply)
        repl=ReplyModel(contactus_id=contactus ,email=email,reply=reply)
        repl.save()
        conct=ContactUsmodel(repl="1")
        conct.save()
        # print(repl)
        messages.success(request,'Reply Sent !')
        # redirect(reverse('readpost', kwargs={"id": id}))
        return redirect(reverse('reply', kwargs={"id": id}))
    contactmesage=ContactUsmodel.objects.get(id=id)
    replymsgs=ReplyModel.objects.filter(contactus_id=id).order_by('-reply_date')
    return render(request,'reply.html',{'contactmesage':contactmesage,'replymessages':replymsgs })


