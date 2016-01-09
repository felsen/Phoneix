# Django Package Imports:
from django.db import models


# Project App Imports:
from userprofile.models import BaseInfo

class HospitalInfo(BaseInfo):

    """ Storing all the hospital information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)
