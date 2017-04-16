"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import handler404, handler500
from blogsite import settings
from blogsite.sitemaps import blogSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
sitemaps = {
'blog': blogSitemap
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),
  	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    	name='django.contrib.sitemaps.views.sitemap'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'homepage.views.page_not_found'
handler500 = 'homepage.views.server_error'