from django import forms
from .models import Doctor , Appointments 

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointments
        fields = ['date','time','doctor','patient']

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['doctor_name','doctor_specialization']
    
    