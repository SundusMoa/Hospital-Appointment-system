from django.urls import path
from . import views


urlpatterns = [ #routing my page ;)
    path('',views.homepage , name = 'homepage' ),
    path('appointment/', views.appointment_list,name='appointment_list'),
    path('appointment/create', views.appointment_create , name='appointment_create'),
    path('appointment/<int:pk>/edit', views.appointment_update, name='appointment_update'),
    path('appointment/<int:pk>/delete', views.appointment_delete, name='appointment_delete'),

    path('doctor/',views.doctor_list,name='doctor_list'),
    path('doctor/create', views.doctor_create , name='doctor_create'),
    path('doctor/<int:pk>/delete', views.doctor_delete, name='doctor_delete'),

]
