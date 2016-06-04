__author__ = 'Kamil Mowinski'


from django.contrib import admin
from HandyMan.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)