__author__ = 'Kamil Mowinski'


from django.views.generic import TemplateView, ListView

from HandyMan.models import Photo



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['photos'] = list(Photo.objects.order_by('?')[:4])
        return ctx


class AboutView(TemplateView):
    template_name = 'about.html'


class ServicesView(TemplateView):
    template_name = 'services.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class GalleryView(ListView):
    model = Photo
    template_name = 'gallery.html'