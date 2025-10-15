from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.doctor_name

class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('doctor', 'date', 'time')

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.doctor_name} on {self.date} {self.time}"
