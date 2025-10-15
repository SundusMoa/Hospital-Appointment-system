from django.shortcuts import render , redirect
from .models import Appointments , Doctor
from .forms import AppointmentForm , DoctorForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage (request):
    return render (request , 'home.html')

@login_required
def appointment_list(request):
    if not is_doctor(request.user):
        # You can either redirect or show a "403 Forbidden" message
        return redirect('myappointment_list') 
    appointments = Appointments.objects.all()
    return render(request, "appointment/appointment_list.html", {"appointments": appointments})
    
def myappointment_list(request):
    u_appointment = Appointments.objects.filter(patient=request.user)
    return render (request , 'appointment/appointment_list.html', {'appointments': u_appointment})

@login_required
def appointment_create(request):
    if request.method == 'GET':
        form = AppointmentForm(user=request.user)
        return render(request, 'appointment/appointment-form.html', {'form': form})

    elif request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user 
            appointment.save()
            return redirect(reverse('myappointment_list'))
        return render(request, 'appointment/appointment-form.html', {'form': form})


def appointment_update(request,pk):
    u_appointment = Appointments.objects.get(pk = pk) 
    if request.method == 'GET':
        form = AppointmentForm(instance = u_appointment) 
        return render(request, 'appointment/appointment-form.html', {'form':form})  
    elif request.method == 'POST':
        form = AppointmentForm(request.POST, instance= u_appointment)
        if form.is_valid(): 
            form.save()
            return redirect (reverse('appointment_list'))

def appointment_delete(request,pk):
    u_appointment = Appointments.objects.get(pk = pk) 
    if request.method == 'POST':
        u_appointment.delete()
        return redirect (reverse('appointment_list'))


def doctor_list (request):
    all_doctor = Doctor.objects.all()
    return render (request , 'doctor/doctor_list.html', {'doctors':all_doctor})



def doctor_create(request):
    if not is_doctor(request.user):
        return redirect('homepage') 
    if request.method == 'GET':
        form = DoctorForm()
        return render (request,'doctor/doctor-form.html',{'form': form})

    elif request.method == 'POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (reverse('doctor_list')) # reverse take name in path
        else :
            return render (request,'doctor/doctor-form.html',{'form': form})
        

def doctor_delete(request,pk):
    u_delete = Doctor.objects.get(pk = pk) 
    if request.method == 'POST':
        u_delete.delete()
        return redirect (reverse('doctor_list'))


def doctor_appointments(request):

    doctor = Doctor.objects.filter(doctor_name=request.user.username).first()
    if doctor:
        appointments = Appointments.objects.filter(doctor=doctor)
    else:
        appointments = []
    return render(request, 'appointment/doctor_appointments.html', {'appointments': appointments})

from django.contrib.auth.forms import UserCreationForm # form to create anew user
from django.contrib.auth.models import User # this is  a built in user models
from django.views.generic import CreateView

# to create a user in my database
class SignUpView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = '/auth/login'  # or your home


# view to render the appointments for only doctor by 
def is_doctor(user):
    return Doctor.objects.filter(doctor_name=user.username).exists()

def some_view(request):
    return render(request, 'base.html', {'is_doctor': is_doctor(request.user)})





