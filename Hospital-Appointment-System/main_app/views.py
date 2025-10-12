from django.shortcuts import render , redirect
from .models import Appointments , Doctor
from .forms import AppointmentForm
from django.urls import reverse
# Create your views here.

def homepage (request):
    return render (request , 'home.html')

def appointment_list (request):
    all_appointment = Appointments.objects.all()
    return render (request , 'appointment/appointment_list.html', {'appointments': all_appointment})
    

def appointment_create(request):
    
    if request.method == 'GET':
        form = AppointmentForm()
        return render (request,'appointment/appointment-form.html',{'form': form})

    elif request.method == 'POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (reverse('appointment_create')) # reverse take name in path
        else :
            return render (request,'appointment/appointment-form.html',{'form': form})

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


