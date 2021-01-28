from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import contactformemail
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'bridgeqe/index.html')


def about(request):
	return render(request, 'bridgeqe/about.html')


def project(request):
	return render(request, 'bridgeqe/project.html')


def gallery(request):
	return render(request, 'bridgeqe/gallery.html')


def contact(request):
	if request.method == 'GET':
		form = contactformemail()
				
	else:
		form = contactformemail(request.POST)
		if form.is_valid():
			frommail   = form.cleaned_data['email']
			subject    = form.cleaned_data['subject']
			message    = form.cleaned_data['message']
			send_mail(subject,message,frommail,['bridgeqeafrica@gmail.com',frommail])
	return render(request, 'bridgeqe/contact.html',{'form':form})