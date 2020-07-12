from django.shortcuts import render,redirect
from . models import Contact
from demo.settings import EMAIL_HOST_USER
from . forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def sendmail(request):

    contact_detail = Contact.objects.last()
    template = 'contact/contact.html'
    
    if request.method == 'POST':
        
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            recepient = str(contact_form['email'].value())

            try : 
                sm(subject,
                message ,EMAIL_HOST_USER,[recepient] ,fail_silently=False)
            
            except BadHeaderError : 
                return HttpResponse('ivalid header')

            return render(request,'contact/contact.html',{'subject':subject})
        

    else:
        contact_form = ContactForm
    
    context ={
        'contact_detail':contact_detail,
        'contact_form':contact_form
        
    }
    
    return render(request, template , context)


def success(request):
    return render(request,'contact/success.html')














