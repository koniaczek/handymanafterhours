__author__ = 'Kamil Mowinski'

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from HandyMan import views



urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about', views.AboutView.as_view(), name='about'),
    url(r'^gallery', views.GalleryView.as_view(), name='gallery'),
    url(r'^services', views.ServicesView.as_view(), name='services'),
    url(r'^contact', views.ContactView.as_view(), name='contact'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

