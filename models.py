from django.db import models
from django.utils import timezone

class PatientSignup(models.Model):
    username=models.CharField(max_length=20)
    full_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class DoctorSignup(models.Model):
    username=models.CharField(max_length=20)
    full_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    specialization=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    patient = models.ForeignKey(PatientSignup, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(DoctorSignup, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.CharField(max_length=200)
    medical_history = models.TextField(blank=True, null=True, help_text="Patient's medical history relevant to this appointment")
    notes = models.TextField(blank=True, null=True, help_text="Doctor's notes about the appointment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name} - {self.appointment_date}"

class Prescription(models.Model):
    patient = models.ForeignKey(PatientSignup, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(DoctorSignup, on_delete=models.CASCADE, related_name='prescriptions')
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions')
    diagnosis = models.CharField(max_length=200)
    medications = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    follow_up_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.diagnosis} - {self.created_at.strftime('%Y-%m-%d')}"

class MedicalRecord(models.Model):
    RECORD_TYPE_CHOICES = (
        ('lab_test', 'Laboratory Test'),
        ('imaging', 'Imaging'),
        ('surgery', 'Surgery'),
        ('general', 'General Checkup'),
        ('other', 'Other'),
    )
    
    patient = models.ForeignKey(PatientSignup, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(DoctorSignup, on_delete=models.CASCADE, related_name='medical_records')
    record_type = models.CharField(max_length=20, choices=RECORD_TYPE_CHOICES)
    record_date = models.DateField()
    description = models.TextField()
    file = models.FileField(upload_to='medical_records/', null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.patient.full_name} - {self.record_type} - {self.record_date}"


