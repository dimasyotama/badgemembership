from django.contrib import admin
from badge_membership.models import PromoCode,Toko,BadgeName,MemberPrivilege,Profile

# Register your models here.

admin.site.register(PromoCode)
admin.site.register(Toko)
admin.site.register(BadgeName)
admin.site.register(MemberPrivilege)
admin.site.register(Profile)