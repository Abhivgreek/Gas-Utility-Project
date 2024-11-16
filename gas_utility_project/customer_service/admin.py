from django.contrib import admin
from .models import Customer, SupportRep, ServiceRequest

admin.site.register(Customer)
admin.site.register(SupportRep)
admin.site.register(ServiceRequest)