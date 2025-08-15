import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hms.settings')
django.setup()

# Now import the model after Django is configured
from hospital.models import Hospital

# List of top hospitals in India
top_hospitals = [
    {
        'name': 'All India Institute of Medical Sciences (AIIMS)',
        'location': 'New Delhi',
        'speciality': 'Multi-specialty',
        'rating': 4.8,
        'description': 'AIIMS is a premier medical institution in India known for its excellence in patient care, teaching, and research. It offers comprehensive healthcare services across all specialties.',
        'image_url': 'https://www.aiims.edu/images/slider/aiims_main.jpg'
    },
    {
        'name': 'Apollo Hospitals',
        'location': 'Chennai',
        'speciality': 'Multi-specialty',
        'rating': 4.7,
        'description': 'Apollo Hospitals is one of the largest healthcare groups in Asia with hospitals across India. Known for advanced medical technology and skilled healthcare professionals.',
        'image_url': 'https://www.apollohospitals.com/wp-content/themes/apollohospitals/assets-v3/images/apollo-hospitals-building.jpg'
    },
    {
        'name': 'Fortis Hospital',
        'location': 'Mumbai',
        'speciality': 'Cardiac Care',
        'rating': 4.6,
        'description': 'Fortis Hospital is renowned for its cardiac care and other specialties. It has state-of-the-art facilities and experienced medical professionals.',
        'image_url': 'https://www.fortishealthcare.com/images/hospitals/fortis-hospital-mulund-mumbai.jpg'
    },
    {
        'name': 'Medanta - The Medicity',
        'location': 'Gurugram',
        'speciality': 'Multi-specialty',
        'rating': 4.7,
        'description': 'Medanta is a multi-specialty medical institute led by highly experienced healthcare professionals. It combines the best medical practices with cutting-edge technology.',
        'image_url': 'https://www.medanta.org/storage/app/media/uploaded-files/medanta-the-medicity-gurugram.jpg'
    },
    {
        'name': 'Tata Memorial Hospital',
        'location': 'Mumbai',
        'speciality': 'Cancer Care',
        'rating': 4.8,
        'description': 'Tata Memorial Hospital is a specialized cancer treatment and research center. It is one of the leading cancer care hospitals in Asia.',
        'image_url': 'https://tmc.gov.in/tmh/images/gallery/TMH_Building.jpg'
    },
    {
        'name': 'Christian Medical College (CMC)',
        'location': 'Vellore',
        'speciality': 'Multi-specialty',
        'rating': 4.6,
        'description': 'CMC Vellore is one of the oldest and most prestigious medical institutions in India known for its excellence in medical education, research, and patient care.',
        'image_url': 'https://www.cmch-vellore.edu/sites/default/files/Hospital%20Main.jpg'
    },
    {
        'name': 'Narayana Health',
        'location': 'Bangalore',
        'speciality': 'Cardiac Care',
        'rating': 4.5,
        'description': 'Narayana Health is known for affordable yet high-quality cardiac care. Founded by Dr. Devi Shetty, it has revolutionized cardiac surgeries in India.',
        'image_url': 'https://www.narayanahealth.org/sites/default/files/nh-health-city-bangalore.jpg'
    },
    {
        'name': 'Kokilaben Dhirubhai Ambani Hospital',
        'location': 'Mumbai',
        'speciality': 'Multi-specialty',
        'rating': 4.7,
        'description': 'Kokilaben Hospital is a state-of-the-art multi-specialty hospital with advanced medical technology and expert healthcare professionals.',
        'image_url': 'https://www.kokilabenhospital.com/images/kdah-building.jpg'
    },
    {
        'name': 'Manipal Hospitals',
        'location': 'Bangalore',
        'speciality': 'Multi-specialty',
        'rating': 4.5,
        'description': 'Manipal Hospitals is a leading healthcare brand with a network of hospitals across India. Known for comprehensive healthcare services and medical education.',
        'image_url': 'https://www.manipalhospitals.com/uploads/2022/02/manipal-hospital-old-airport-road-bangalore.jpg'
    },
    {
        'name': 'Lilavati Hospital',
        'location': 'Mumbai',
        'speciality': 'Multi-specialty',
        'rating': 4.6,
        'description': 'Lilavati Hospital is a multi-specialty tertiary care hospital known for its excellent medical services and patient care.',
        'image_url': 'https://www.lilavatihospital.com/assets/frontend/images/lilavati-hospital.jpg'
    }
]

def add_hospitals():
    # Clear existing hospitals
    Hospital.objects.all().delete()
    
    # Add new hospitals
    for hospital_data in top_hospitals:
        Hospital.objects.create(
            name=hospital_data['name'],
            location=hospital_data['location'],
            speciality=hospital_data['speciality'],
            rating=hospital_data['rating'],
            description=hospital_data['description'],
            image_url=hospital_data['image_url']
        )
    
    print(f"Added {len(top_hospitals)} hospitals to the database.")

if __name__ == "__main__":
    add_hospitals()