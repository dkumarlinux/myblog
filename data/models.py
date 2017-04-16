from django.db import models
from django.db.models.signals import post_save
#from django.core.signals import request_finished
from data.managers import EntryManager
from . import handlers
from homepage.signals import message_sent

class Entry(models.Model):
	created=models.DateTimeField(auto_now_add=True, null=True)
	updated=models.DateTimeField(auto_now=True, null=True)
	title=models.CharField(max_length=140)
	image=models.FileField(null=True, blank=True)
	text=models.TextField()
	published=models.BooleanField(default=True)
	objects = EntryManager()
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/" %(self.id)

 

#request_finished.connect(handlers.request_finished)
post_save.connect(handlers.model_save, sender=Entry)
message_sent.connect(handlers.request_finished)