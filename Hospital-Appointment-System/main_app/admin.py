from django.contrib import admin
from .models import Doctor , Appointments

# Register your models here.
admin.site.register(Appointments)
admin.site.register(Doctor)
