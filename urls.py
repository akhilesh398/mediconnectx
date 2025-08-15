"""
URL configuration for Hms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hms import views
from hospital import views as hospital_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome, name='home'),
    path('login/',views.patient_login, name='login'),
    path('patientsignup/',views.mysignup, name='patient_signup'),
    path('doctorsignup/',views.doctor_sign, name='doctor_signup'),
    path('doctorlogin/',views.doctor_login, name='doctor_login'),
    path('contact/',views.mycontact, name='contact'),
    path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/patient/', views.logout_patient, name='logout_patient'),
    path('logout/doctor/', views.logout_doctor, name='logout_doctor'),
    
    # Patient pages
    path('patient/appointments/', hospital_views.patient_appointments, name='patient_appointments'),
    path('patient/prescriptions/', hospital_views.patient_prescriptions, name='patient_prescriptions'),
    path('patient/medical-records/', hospital_views.patient_medical_records, name='patient_medical_records'),
    path('patient/find-doctors/', hospital_views.find_doctors, name='find_doctors'),
    path('patient/profile/', hospital_views.patient_profile, name='patient_profile'),
    
    # Doctor pages
    path('doctor/appointments/', hospital_views.doctor_appointments, name='doctor_appointments'),
    path('doctor/prescriptions/', hospital_views.doctor_prescriptions, name='doctor_prescriptions'),
    path('doctor/patients/', hospital_views.doctor_patients, name='doctor_patients'),
    path('doctor/profile/', hospital_views.doctor_profile, name='doctor_profile'),
    
    # API endpoints
    path('patient/get_appointment_details/<int:appointment_id>/', hospital_views.patient_get_appointment_details, name='patient_get_appointment_details'),
    path('doctor/get_appointment_details/<int:appointment_id>/', hospital_views.get_appointment_details, name='doctor_get_appointment_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
