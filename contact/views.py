from django.shortcuts import render,redirect
from . models import Contact
from demo.settings import EMAIL_HOST_USER
from . forms import ContactForm 
from django.core.mail import send_mail ,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def sendmail(request):
    
    
    if request.method == 'POST':
        
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
            

        #try : 
        send_mail(subject,
        message ,email,[EMAIL_HOST_USER],fail_silently=False )
            

        return render(request,'contact/contact.html',{'subject':subject})
        

    else: 
        return render(request,'contact/contact.html' )


def success(request):
    return render(request,'contact/success.html')














