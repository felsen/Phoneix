# Django package Imports:
from django.contrib import admin

# From ThirdParty Package Imports:

# From Local Projects Imports:
from userprofile.models import UserGetList

admin.site.register(UserGetList)
