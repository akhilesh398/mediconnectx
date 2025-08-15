from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from hospital.models import PatientSignup, DoctorSignup
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Health tools imports
from datetime import datetime
import json
import math


def myhome(request):
    return render(request,'home.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            patient = PatientSignup.objects.get(username=username, password=password)
            # Store patient info in session
            request.session['patient_id'] = patient.id
            request.session['patient_username'] = patient.username
            request.session['patient_name'] = patient.full_name
            return redirect('/user/dashboard/')
        except PatientSignup.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request, 'patient_login.html', {'error_message': error_message})
    
    return render(request,'patient_login.html')

def patient_sign(request):
    return render(request,'patient_signup.html')

def doctor_sign(request):
    if request.method == 'POST':
        username = request.POST['username']
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        specialization = request.POST['specialization']
        city = request.POST['city']
        password = request.POST['password']

        doctor = DoctorSignup(username=username, full_name=full_name, email=email, phone=phone, 
                           specialization=specialization, city=city, password=password)
        doctor.save()
        
        # Store doctor info in session and redirect to dashboard
        request.session['doctor_id'] = doctor.id
        request.session['doctor_username'] = doctor.username
        request.session['doctor_name'] = doctor.full_name
        request.session['doctor_specialization'] = doctor.specialization
        
        subject = 'Welcome to MediConnectX – Thank You for Registering!'
        message = f'''
Dear {full_name},

Thank you for registering with MediConnectX – your trusted partner in smart healthcare solutions.

We’re excited to have you on board! Your registration has been successfully completed.

With MediConnectX, you can:
✅ Book doctor appointments with ease  
✅ Access your medical records anytime  
✅ Stay connected with top hospitals and healthcare providers  

If you have any questions or need assistance, feel free to reach out to our support team at mediconnectx@gmail.com.

Stay healthy, stay connected.

Warm regards,  
Team MediConnectX  
www.mediconnectx.com
        '''
        from_email = 'mediconnectx@gmail.com' 
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            print("Email error:", e)
        return redirect('/doctorlogin')
    return render(request,'doctor_signup.html')

def mycontact(request):
    return render(request,'contact.html')

def user_dashboard(request):
    if 'patient_id' not in request.session:
        return redirect('/login/')
    
    patient_id = request.session['patient_id']
    patient = PatientSignup.objects.get(id=patient_id)
    
    context = {
        'patient': patient
    }
    
    return render(request, 'user_dashboard.html', context)

def logout_patient(request):
    if 'patient_id' in request.session:
        del request.session['patient_id']
    return redirect('/')

def doctor_dashboard(request):
    if 'doctor_id' not in request.session:
        return redirect('/doctorlogin/')
    
    doctor_id = request.session['doctor_id']
    doctor = DoctorSignup.objects.get(id=doctor_id)
    
    context = {
        'doctor': doctor
    }
    
    return render(request, 'doctor_dashboard.html', context)

def logout_doctor(request):
    if 'doctor_id' in request.session:
        del request.session['doctor_id']
    return redirect('/')

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            doctor = DoctorSignup.objects.get(username=username, password=password)
            # Store doctor info in session
            request.session['doctor_id'] = doctor.id
            request.session['doctor_username'] = doctor.username
            request.session['doctor_name'] = doctor.full_name
            request.session['doctor_specialization'] = doctor.specialization
            return redirect('/doctor/dashboard/')
        except DoctorSignup.DoesNotExist:
            error_message = "Invalid username or password"
            
            return render(request, 'doctor_login.html', {'error_message': error_message})
    
    return render(request,'doctor_login.html')


def mysignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        full_name = request.POST['full_name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        city=request.POST['city']
        password=request.POST['password']

        s1 = PatientSignup(username=username, full_name=full_name, email=email, mobile=mobile, city=city, password=password)
        s1.save()
        
        # Store patient info in session and redirect to dashboard
        request.session['patient_id'] = s1.id
        request.session['patient_username'] = s1.username
        request.session['patient_name'] = s1.full_name

        subject = 'Welcome to MediConnectX – Thank You for Registering!'
        message = f'''
Dear {full_name},

Thank you for registering with MediConnectX – your trusted partner in smart healthcare solutions.

We’re excited to have you on board! Your registration has been successfully completed.

With MediConnectX, you can:
✅ Book doctor appointments with ease  
✅ Access your medical records anytime  
✅ Stay connected with top hospitals and healthcare providers  

If you have any questions or need assistance, feel free to reach out to our support team at mediconnectx@gmail.com.

Stay healthy, stay connected.

Warm regards,  
Team MediConnectX  
www.mediconnectx.com
        '''
        from_email = 'mediconnectx@gmail.com' 
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except Exception as e:
            print("Email error:", e) 

        return redirect('/login')
    return render(request,'patient_signup.html')
    
def mylogin(request):
    return render(request,'login.html')