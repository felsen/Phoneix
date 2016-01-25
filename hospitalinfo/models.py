# Django Package Imports:
from django.db import models
from django.template.defaultfilters import slugify

# Project App Imports:
from userprofile.models import BaseInfo

class HospitalInfo(BaseInfo):

    """ Storing all the hospital information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    addr = models.TextField(max_length = 500, default = None)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')
    slug = models.SlugField('URL4SEO', blank = True, null = True)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(HospitalInfo, self).save(*args, **kwargs)

class DoctorsInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    addr = models.TextField(max_length = 500, default = None)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/admin_static/dist/img/pic.jpg')
    slug = models.SlugField('URL4SEO', blank = True, null = True)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DoctorsInfo, self).save(*args, **kwargs)

class ClinicInfo(BaseInfo):

    """ Storing all the clinic information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    addr = models.TextField(max_length = 500, default = None)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')
    slug = models.SlugField('URL4SEO', blank = True, null = True)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ClinicInfo, self).save(*args, **kwargs)

class DgLabsInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    addr = models.TextField(max_length = 500, default = None)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')
    slug = models.SlugField('URL4SEO', blank = True, null = True)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DgLabsInfo, self).save(*args, **kwargs)

class PharmacyInfo(BaseInfo):

    """ Storing all the doctors information. """

    name = models.CharField(max_length = 50)
    desc = models.TextField(max_length = 500)
    addr = models.TextField(max_length = 500, default = None)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    spacility = models.TextField(max_length = 100)
    image = models.ImageField(upload_to = 'static/%Y_%m_%d/', default='static/img/icons_healthcare.png')
    slug = models.SlugField('URL4SEO', blank = True, null = True)

    def __unicode__(self):
        return "%s - %s"%(self.name, self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PharmacyInfo, self).save(*args, **kwargs)
