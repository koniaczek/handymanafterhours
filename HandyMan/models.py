__author__ = 'Kamil Mowinski'

from django.utils.safestring import mark_safe
from django.db import models
from django.utils.translation import ugettext_lazy as _
from thumbnailfield.fields import ThumbnailField

class Photo(models.Model):
    thumbnail = ThumbnailField(_('thumbnail'), upload_to='img/thumbnails',
                               pil_save_options={'quality': 100},
                               patterns={
                                   'tiny': (130, 130),
                               })

    def __str__(self):
        return mark_safe('<img src="{}" />'.format(self.thumbnail.tiny.url))

    def image_tag(self):
        return mark_safe('<img src="{}" />'.format(self.thumbnail.tiny.url))