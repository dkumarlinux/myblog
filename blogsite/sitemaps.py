# Site error:
#Open the Django shell for your site (python3.5 manage.py shell).
#>>> from django.contrib.sites.models import Site
#>>> Site.objects.create(name='blogsite.com', domain='127.0.0.1:8000')

from django.contrib.sitemaps import Sitemap
from data.models import Entry

class blogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return "/"

