from distutils.log import error
from logging import raiseExceptions
from django.shortcuts import render
from email_app.forms import ContactMeForm
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    form=ContactMeForm()
    if request.method=='POST':
        form=ContactMeForm(request.POST)
        if form.is_valid():
            subject='contact form inquiry'
            body={
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email_id':form.cleaned_data['email_id'],
                'subject':form.cleaned_data['subject'],
                'message':form.cleaned_data['message'],
            }
            message='\n'.join(body.values())
            sender=form.cleaned_data['email_id']
            recipient=['abc@gmail.com']
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
                return HttpResponse('<h1>message send sucessfully</h1>')
            except:
                return HttpResponse('<h1>Bad message format</h1>')
    return render(request, "home/index.html",{'form':form})
