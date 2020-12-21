from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=256)
    event_text = models.TextField(blank = True)
    data_pub = models.DateField()
    active = models.BooleanField(verbose_name="Active")
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    #def __unicode__(self):
        #return "{title}".format(title=self.title)

    #def get_absolute_url(self):  # dodane w zwiazku z kalendarzem sluzy do okreslania adresu
     #   return "/artykul/%i/" % self.id
