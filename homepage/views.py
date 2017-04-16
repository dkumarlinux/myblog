from urllib.parse import quote 
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from data.models import Entry
from .forms import contactForm
from django.contrib.sitemaps import Sitemap
from . import signals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
#	entries = Entry.objects.published_entries().order_by('-id') # by managers.py
	
	entries = Entry.objects.all().order_by('-id')
	query = request.GET.get("q")
# For Query from title,text etc.
	if query:
		entries = entries.filter(
			Q(title__icontains=query)|
			Q(text__icontains=query)
			).distinct()

	paginator = Paginator(entries, 10)
	page_num = request.GET.get('page',1)
	try:
		page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		page = paginator.page(1)


	context = {
		'page':page
	}
	return render(request,"homepage/posts.html", context)

def about(request):
	return render(request,"homepage/about.html")

def archive(request):
	page = Entry.objects.all()
	
	return render(request,"homepage/archive.html",{'page':page})

def posts(request):
	page = Entry.objects.all().order_by('-id')
	
	return render(request,"homepage/list.html",{'page':page})

def post_details(request, id=None):
#	instance = Entry.objects.get(id=30)	
	instance = get_object_or_404(Entry, id=id )
	context ={
		"title":instance.title,
		"instance":instance,
		
	}
	return render(request, "homepage/post_details.html", context)



def contact(request):
	title='Contact'
	form = contactForm(request.POST or None)
	confirm_message=None

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject ='Message from myblog.com'
		message='%s %s' %(comment, name,)
		emailFrom=form.cleaned_data['email']
		emailTo=[settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		signals.message_sent.send(sender=contact, email=emailFrom)
		title="Thanks!."
		confirm_message="Thanks for the message. We will get right back to you."
		form=None
	
	context={'title':title, 'form':form, 'confirm_message':confirm_message,}
	template='homepage/contact.html'
	return render(request, template, context)

# these functions for bad request page 
def page_not_found(request):
	return render(request,'homepage/404.html')


def server_error(request):
	return render(request,'homepage/500.html')

