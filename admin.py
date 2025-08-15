from django.contrib import admin
from .models import PatientSignup, DoctorSignup, Hospital, Appointment, Prescription, MedicalRecord

# Register your models here.
admin.site.register(PatientSignup)
admin.site.register(DoctorSignup)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(MedicalRecord)
