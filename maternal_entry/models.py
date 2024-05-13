from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class MaternalEntry(models.Model):
    
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
    
    MULTI_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont know', 'Dont Know'),
    ]
    
    HIV_STATUS_CHOICES = [
        ('reactive', 'Reactive'),
        ('non-reactive', 'Non-reactive'),
        ('dont know', 'Dont Know'),
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
    hiv_status = models.CharField(max_length=50, choices=HIV_STATUS_CHOICES, default="non-reactive")
    date_of_arrival = models.DateField()
    time_of_arrival = models.TimeField()
    time_treatment_started = models.TimeField()
    referral_from_another_facility = models.CharField(max_length=50, choices=MULTI_CHOICES, default="no")
    
    
    