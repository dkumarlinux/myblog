from django.contrib.syndication.views import Feed
from data.models import Entry


class ArchiveFeed(Feed):
	title="Archive Feed"
	description="Archive Feed"
	link="/archive/"

	def items(self): # to get data
		return Entry.objects.filter(published=True).order_by('-id')[:25]

	def item_link(self, item):
		return "/archive/"
		
#	def item_title(self, item):
#		return item.title

#	def item_description(self, item):
#		return item.text