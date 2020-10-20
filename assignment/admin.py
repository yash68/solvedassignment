from django.contrib import admin
from .models import PaymentDetails, AssignmentDetails, RequestedAssignment
# Register your models here.

admin.site.register(PaymentDetails)
admin.site.register(AssignmentDetails)
admin.site.register(RequestedAssignment)