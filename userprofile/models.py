from django.db import models


class BaseInfo(models.Model):

    """ This will provide the common field for all the inherited classes """

    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        abstract = True

class UserGetList(BaseInfo):

    """ Collecting the user information before login """

    username = models.CharField('Name', max_length=50, blank=True)
    email = models.EmailField('Email', max_length=254,blank=True)
    phone_no = models.IntegerField('Phone', blank = True, null = True)
    organization_name = models.CharField('Organization Name', max_length=50, blank=True)
    address = models.TextField('Address', max_length = 750, blank = True, null = True)
    website = models.URLField('Website', blank = True)

    def __unicode__(self):
        return "%s- %s"%(self.username, self.email)
