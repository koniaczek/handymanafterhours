from django.views.generic import TemplateView

__author__ = 'kamil'


class HomeView(TemplateView):
    template_name = 'index.html'