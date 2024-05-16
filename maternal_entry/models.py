from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from facility_creation.models import Region, District, Facility


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
        ('others (specify)', 'Others (Specify)'),
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
    
    MODE_OF_DELIVERY_CHOICES = [
        ('spontaneous vaginal delivery', 'Spontaneous Vaginal Delivery'),
        ('vacuum/forceps', 'Vacuum/forceps'),
        ('caesarian section', 'Caesarian section'),        
    ]
    
    DELIVERY_OUTCOMES_CHOICES = [
        ('live birth', 'Live Birth (irrespective of gestation)'),
        ('fresh stillbirth', 'Fresh Stillbirth'),
        ('macerated stillbirth', 'Macerated Stillbirth'),
        ('early neonatal death', 'Early Neonatal Death (within 24 hours)'),                
    ]
    
    
    EARLY_PREGNANCY_CHOICES = [
        ('evacuation', 'Evacuation'),
        ('antibiotic therapy', 'Antibiotic Therapy'),
        ('laparotomy', 'Laparotomy'),
        ('hysterectomy', 'Hysterectomy'),
        ('transfusion', 'Transfusion'),                
        ('anti hypertensive', 'Anti Hypertensive'),                
    ]
    
    ANTENATAL_CHOICES = [
        ('transfusion', 'Transfusion'),
        ('antibiotic therapy', 'Antibiotic Therapy'),
        ('external version', 'External version'),
        ('mag sulphate', 'Mag. Sulphate'),
        ('diazepam', 'Diazepam'),                
        ('anti hypertensive', 'Anti Hypertensive'),
        ('hysterectomy', 'Hysterectomy'),            
    ]
    
    
    INTRAPARTUM_CHOICES = [
        ('instrumental del', 'Instrumental del.'),
        ('antibiotic therapy', 'Antibiotic Therapy'),
        ('caesarian section', 'Caesarian section'),
        ('hysterectomy', 'Hysterectomy'),
        ('transfusion', 'Transfusion'),            
        ('mag sulphate', 'Mag. Sulphate'),
        ('anti hypertensive', 'Anti Hypertensive'),
        ('diazepam', 'Diazepam'),                
    ]
    
    
    POSTPARTUM_CHOICES = [
        ('evacuation', 'Evacuation'),
        ('antibiotic therapy', 'Antibiotic Therapy'),
        ('laparotomy', 'Laparotomy'),
        ('hysterectomy', 'Hysterectomy'),
        ('transfusion', 'Transfusion'),            
        ('manual removal of placenta', 'Manual removal of placenta'),
        ('anti hypertensive', 'Anti Hypertensive'),
        ('diazepam', 'Diazepam'),                
    ]
    
    
    OTHER_OPTIONS = [
        ('anaesthesia-GA', 'Anaesthesia-GA'), 
        ('epidural', 'Epidural'),                
        ('spinal', 'Spinal'),                
        ('local', 'Local'),                
        ('invasive monitoring', 'Invasive monitoring'),
        ('anti hypertensive', 'Anti Hypertensive'),             
        ('ICU ventilation', 'ICU ventilation'),                               
    ]
    
    AUTOPSY_PERFORMED_BY_CHOICES = [
        ('pathologist', 'Pathologist'),                
        ('medical officer', 'Medical Officer'),                
        ('others (specify)', 'Others (Specify)'),
    ]
    
    
    PRIMARY_OBSTETRIC_COD_CHOICES = [
        ('haemorrhage', 'Haemorrhage'),                
        ('unsafe abortion', 'Unsafe abortion'),                
        ('ruptured uterus ', 'Ruptured Uterus '),                
        ('obstructed labour', 'Obstructed Labour'),                
        ('malaria', 'Malaria'),                
        ('hypertensive disease', 'hypertensive disease'),                
        ('genital tract sepsis', 'Genital Tract Sepsis'),                
        ('ectopic pregnancy', 'Ectopic Pregnancy'),
        ('sickle cell disease', 'Sickle Cell disease'),                
    ]
    
    AUDITED_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    
    facility_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    facility_district = models.ForeignKey(District, on_delete=models.PROTECT)
    facility_name = models.ForeignKey(Facility, on_delete=models.PROTECT)
    name_of_deceased = models.CharField(max_length=100)
    dob_unknown = models.BooleanField(default=False)
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
    identified_risk_factors = models.TextField(choices=IDENTIFIED_RISK_CHOICES, null=True)        #Multiple select field
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
    delivery_by = models.CharField(max_length=100, choices=DELIVERED_BY_CHOICES, default="midwife", null=True)
    delivery_by_others = models.CharField(max_length=100, default="none", null=True)
    mode_of_delivery = models.CharField(max_length=100, choices=MODE_OF_DELIVERY_CHOICES, null=True)
    delivery_outcome = models.CharField(max_length=100, choices=DELIVERY_OUTCOMES_CHOICES, null=True)
    birth_weight = models.FloatField()
    days_since_termination = models.IntegerField(null=True)
    place_of_death = models.CharField(max_length=100, choices=LOCATION_OF_DELIVERY_CHOICES)
    other_place_of_death = models.CharField(max_length=100, default="none", null=True)
    date_of_death = models.DateField()
    time_of_death = models.TimeField()
    early_pregnancy = models.TextField(choices=EARLY_PREGNANCY_CHOICES, null=True)        #Multiple select field
    antenatal = models.TextField(choices=ANTENATAL_CHOICES, null=True)              #Multiple select field
    intrapartum = models.TextField(choices=INTRAPARTUM_CHOICES, null=True)              #Multiple select field
    postpartum = models.TextField(choices=POSTPARTUM_CHOICES, null=True)              #Multiple select field
    other_options = models.TextField(choices=OTHER_OPTIONS, null=True)
    other_interventions = models.TextField(default="none", null=True)
    #SECTION:G, MORTALITY DETAILS
    autopsy_performed = models.CharField(max_length=50, choices=MULTI_CHOICES)
    date_autopsy_performed = models.DateField()
    place_autopsy_performed = models.CharField(max_length=100, null=True, default="none")
    autopsy_performed_by = models.CharField(max_length=100, choices=AUTOPSY_PERFORMED_BY_CHOICES, null=True)
    other_autopsy_performed_by = models.CharField(max_length=100, default="none", null=True)
    final_COD = models.TextField()
    primary_obstetric_COD = models.TextField(choices=PRIMARY_OBSTETRIC_COD_CHOICES, null=True)    #Multiple select field
    other_primary_obstetric_COD = models.TextField(null=True)    #Multiple select field
    #SECTION:H CONTRIBUTORY FACTORS
    delay_in_seeking_help = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    specify_delay_in_seeking_help = models.CharField(max_length=250, null=True)
    lack_of_transport_from_home = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    specify_lack_of_transport_from_home = models.CharField(max_length=250, null=True)
    lack_of_transport_between_facility = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)
    specify_lack_of_transport_between_facility = models.CharField(max_length=250, null=True)
    hf_communication_breakdown = models.CharField(max_length=50, choices=MULTI_CHOICES, null=True)     #hf - health facility
    specify_hf_communication_breakdown = models.CharField(max_length=250, null=True)                    #hf - health facility
    lessons_learnt = models.TextField()         #What has your facility learnt from this case and what changes have been instituted?
    recommendations = models.TextField()        #Recommendations and Further Actions to be Taken
    isAudited = models.CharField(max_length=100, choices=AUDITED_CHOICES, default="yes")
    #SECTION: I DETAILS OF REPORTERS
    names_of_team_members = models.TextField()
    committee_chairman_name = models.CharField(max_length=100, default="Med Sup")
    committee_chairman_phone = models.CharField(max_length=20, default="0000000000")
    committee_chairman_rank = models.CharField(max_length=100, null=True)
    forms_entered_by = models.CharField(max_length=100)
    last_updated = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.facility_name} - maternal death'
    
    
    
    