from django.contrib import admin
from .models import PaymentDetails, AssignmentDetails, RequestedAssignment, MyProfile
# Register your models here.

admin.site.register(PaymentDetails)
admin.site.register(AssignmentDetails)
admin.site.register(RequestedAssignment)
admin.site.register(MyProfile)