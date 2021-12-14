from django.contrib import admin
from homefix.models import Service_provider, Service_requested, Contact_Us, User_type

# Register your models here.
admin.site.register(Service_provider)
admin.site.register(Service_requested)
admin.site.register(Contact_Us)
admin.site.register(User_type)