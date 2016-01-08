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
    phone_no = models.CharField('Phone', max_length = 10, blank = True, null = True, help_text = "Ex: 8050459876")
    organization_name = models.CharField('Organization Name', max_length=50, blank=True)
    address = models.TextField('Address', max_length = 750, blank = True, null = True)
    website = models.URLField('Website', blank = True, help_text = "Ex:http://www.example.com")

    def __unicode__(self):
        return "%s- %s"%(self.username, self.email)

#    def clean(self, *args, **kwargs):
#        if self.phone_no.isdigit() == False and len(self.phone_no) > 10:
#            raise ValidationError("Enter the valid phone number")
#        super(UserGetList, self).clean(*args, **kwargs)
