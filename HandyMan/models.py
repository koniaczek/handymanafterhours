__author__ = 'kamil'

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Photo(models.Model):
    name = models.CharField(_("Photo name"), max_length=250)
    description = models.TextField(_("Description"))
    file = models.ImageField(_("Images"))
    thumbnail = models.ImageField(_("Thumbnail"), width_field=130, max_length=250)