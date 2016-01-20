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
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)


class DoctorsInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/admin_static/dist/img/pic.jpg')

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)


class ClinicInfo(BaseInfo):

    """ Storing all the clinic information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)


class DgLabsInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)


class PharmacyInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

