from django.db import models

# Create your models here.
class Doctor (models.Model): # class is the table and objects is the rows
    doctor_id = models.BigAutoField (primary_key=True)
    doctor_name = models.CharField(max_length=50 , null=False) # this field CANNOT be null
    doctor_specialization = models.CharField(max_length=50 , null=False)# this field CANNOT be null

    def __self__(self):
        return self.doctor_name

class User (models.Model):
    user_id=models.BigAutoField (primary_key=True)
    user_name= models.CharField(max_length=50 , null=False) # this field CANNOT be null
    user_email=models.EmailField(max_length=254 , null=False) # this field CANNOT
    user_password=models.CharField(max_length=50 , null=False) # this field CANNOT be null  

    def __self__(self):
        return self.user_name 

class Appointments (models.Model):
    patient_name = models.CharField(max_length=50 , null=False) # this field CANNOT be null
    date = models.DateField(null=False) # this field CANNOT be null
    time = models.TimeField(null=False) # this field CANNOT be null

    # the relation is one to many (one doctor can have many appointments & one user can have many appointments)
    doctor = models.ForeignKey(Doctor , related_name='appointments', on_delete=models.CASCADE) # this field can be null
    user = models.ForeignKey(User, related_name='appointments',on_delete=models.CASCADE)

    def __self__(self):
        return self.patient_name