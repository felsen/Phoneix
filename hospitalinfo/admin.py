# Django package Imports:
from django.contrib import admin

# From ThirdParty Package Imports:

# From Local Projects Imports:
from hospitalinfo.models import HospitalInfo, DoctorsInfo, ClinicInfo, DgLabsInfo, PharmacyInfo

admin.site.register(HospitalInfo)
admin.site.register(DoctorsInfo)
admin.site.register(ClinicInfo)
admin.site.register(DgLabsInfo)
admin.site.register(PharmacyInfo)
