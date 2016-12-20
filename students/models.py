from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.ForeignKey(User)
    nationality = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return u'%s %s' %(self.user.first_name, self.user.last_name)
