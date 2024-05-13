from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class MaternalEntry(models.Model):
    
    MULTI_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont know', 'Dont Know'),
    ]
    
    
    DOB_UNKNOWN_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    EDUCATION_CHOICES = [
        ('none', 'None'),
        ('primary', 'Primary'),
        ('middle/JHS', 'Middle/JHS'),
        ('secondary/SHS', 'secondary/SHS'),
        ('tertiary', 'Tertiary'),
        ('dont know', 'Dont Know'),
    ]
    
    OCCUPATION_CHOICES = [
        ('unemployed', 'Unemployed'),
        ('house wife', 'House wife'),
        ('farming', 'Farming'),
        ('trading', 'Trading'),
        ('artisan', 'Artisan(hairdresser, seamstress etc)'),
        ('civil/public servant', 'Civil/Public servant'),
        ('other (specify)', 'Other (Specify)'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('never married', 'Never Married'),
        ('married', 'Married'),
        ('living together', 'Living Together'),
        ('divorced/separated', 'Divorced/Separated'),
        ('widowed', 'Widowed'),
    ]
    
    RELIGION_CHOICES = [
        ('christian', 'Christian'),
        ('muslim', 'Muslim'),
        ('traditionalist/ spiritualist', 'Traditionalist/ Spiritualist'),
        ('others (specify)', 'Others (Specify)'),
    ]
    
    
    ETHNICITY_CHOICES = [
        ('akan', 'Akan'),
        ('ga/dangbe', 'Ga/Dangbe'),
        ('ewe', 'Ewe'),
        ('mole/dagbani', 'Mole/Dagbani'),
        ('grussi', 'Grussi'),
        ('gruma', 'Gruma'),
        ('others (specify)', 'Others (Specify)'),
    ]
    
    
    HIV_STATUS_CHOICES = [
        ('reactive', 'Reactive'),
        ('non-reactive', 'Non-reactive'),
        ('dont know', 'Dont Know'),
    ]
    
    PLACE_OF_ANC_CHOICES = [
        ('teaching hospital', 'Teaching Hospital'),
        ('regional hospital', 'Regional Hospital'),
        ('district hospital', 'District Hospital'),
        ('polyclinic', 'Polyclinic'),
        ('health centre', 'Health Centre'),
        ('clinic', 'Clinic'),
        ('CHPS compound', 'CHPS Compound'),
        ('private maternity home', 'Private Maternity Home'),
        ('others (specify)', 'Others (Specify)'),
        
    ]
    
    IDENTIFIED_RISK_CHOICES = [
        ('none', 'none'),
        ('hypertension', 'Hypertension'),
        ('sickle cell disease', 'Sickle Cell Disease'),
        ('previous caesarean section', 'Previous Caesarean Section'),
        ('diabetes mellitus', 'Diabetes Mellitus'),
        ('anaemia', 'Anaemia (HB < 11 g/dl; most current)'),
        ('previous PPH', 'Previous PPH'),
        ('others (specify)', 'Others (Specify)'),
    ]
    
    TRANSPORT_TYPE_CHOICES = [
        ('ambulance', 'Ambulance'),
        ('hospital vehicle', 'Hospital vehicle (not ambulance)'),
        ('public transport', 'Public Transport'),
        ('private transport', 'Private Transport'),
        ('others (specify)', 'Others (Specify)'),
    ]
    
    
    LOCATION_OF_DELIVERY_CHOICES = [
        ('teaching hospital', 'Teaching Hospital'),
        ('regional hospital', 'Regional Hospital'),
        ('district hospital', 'District Hospital'),
        ('polyclinic', 'Polyclinic'),
        ('health centre', 'Health Centre'),
        ('clinic', 'Clinic'),
        ('CHPS compound', 'CHPS Compound'),
        ('private maternity home', 'Private Maternity Home'),
        ('home', 'Home'),
        ('others (specify)', 'Others (Specify)'),
    ]
    
    
    DELIVERED_BY_CHOICES = [
        ('doctor', 'Doctor'),
        ('midwife', 'Midwife'),
        ('TBA', 'TBA'),
        ('others (specify)', 'Others (Specify)'),
        
    ]
    
    
    name_of_deceased = models.CharField(max_length=100)
    dob_unknown = models.CharField(max_length=20, choices=DOB_UNKNOWN_CHOICES, default="no")
    date_of_birth = models.DateField()
    age = models.IntegerField()
    educational_status = models.CharField(max_length=100, choices=EDUCATION_CHOICES, default="none")
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, default="unemployed")
    other_occupation = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES, default="never married")
    religion = models.CharField(max_length=100, choices=RELIGION_CHOICES, default="christian")
    other_religion = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100, choices=ETHNICITY_CHOICES, default="akan")
    other_ethnicity = models.CharField(max_length=100)
    gravidity = models.CharField(max_length=100)
    parity = models.CharField(max_length=100)
    anc = models.CharField(max_length=50, choices=MULTI_CHOICES, default="yes")
    total_anc_visits = models.IntegerField(default=0)
    place_of_anc = models.CharField(max_length=100, choices=PLACE_OF_ANC_CHOICES)
    other_place_of_anc = models.CharField(max_length=100, default="none")
    gestational_age = models.IntegerField(default="0")
    identified_risk_factors = models.TextField(choices=IDENTIFIED_RISK_CHOICES, null=True)
    other_risk_factors = models.CharField(max_length=100, default="none", null=True)
    hiv_status = models.CharField(max_length=50, choices=HIV_STATUS_CHOICES, default="non-reactive")
    on_ARV = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    date_of_arrival = models.DateField()
    time_of_arrival = models.TimeField()
    time_treatment_started = models.TimeField()
    referral_from_another_facility = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    referral_from_where = models.CharField(max_length=100)
    time_to_reach_facility = models.IntegerField(null=True)
    transport_type = models.CharField(max_length=100, choices=TRANSPORT_TYPE_CHOICES, null=True)
    other_transport_type = models.CharField(max_length=100, null=True)
    labour_occur = models.CharField(max_length=50, choices=MULTI_CHOICES, default="no")
    labour_induced = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    labour_augmented = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    photograph_used = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    active_phase = models.IntegerField(default=0, null=True)
    second_stage = models.IntegerField(default=0, null=True)
    third_stage= models.IntegerField(default=0, null=True)
    patient_deliver = models.CharField(max_length=50, choices=MULTI_CHOICES, default="no")
    location_of_delivery = models.CharField(max_length=100, choices=LOCATION_OF_DELIVERY_CHOICES, null=True)
    other_location_of_delivery = models.CharField(max_length=100, default="none", null=True)
    delivery_by = models.CharField(max_length=100, choices=DELIVERED_BY_CHOICES, default="none", null=True)
    delivery_by_others = models.CharField(max_length=100, default="none", null=True)
    
    