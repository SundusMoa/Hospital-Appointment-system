from django import forms
from .models import Doctor , Appointments 

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointments
        fields = ['date','time','doctor','patient']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['patient'].initial = user.id
 

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['doctor_name','doctor_specialization']
    
    