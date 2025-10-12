from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage ),
    path('appointment/', views.appointment_list,name='appointment_list'),
    path('appointment/create', views.appointment_create , name='appointment_create'),
    path('appointment/<int:pk>/edit', views.appointment_update, name='appointment_update')
]
