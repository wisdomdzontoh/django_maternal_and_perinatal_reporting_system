from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from facility_creation.models import Region, District, Facility
from .models import MaternalEntry


@login_required(login_url="authentication:my-login")
def index(request):
    return render(request, 'maternal_entry/index.html')


@login_required(login_url="authentication:my-login")
def add_new(request):
    regions = Region.objects.all()
    districts = District.objects.all()
    context = {
        'regions': regions,
        'districts': districts,
    }
    
    if request.method == 'POST':
        facility_region_id = request.POST.get("facility_region")
        facility_district_id = request.POST.get("facility_district")
        facility_name_id = request.POST.get("facility_name")
        name_of_deceased = request.POST.get("name_of_deceased")
        dob_unknown = request.POST.get("dob_unknown") == 'on'
        date_of_birth = request.POST.get("date_of_birth")
        age = request.POST.get('age', None)
        if age == '':
            age = None  # Convert empty string to None
        educational_status = request.POST.get("educational_status")
        occupation = request.POST.get("occupation")
        other_occupation = request.POST.get("other_occupation")
        marital_status = request.POST.get("marital_status")
        religion = request.POST.get("religion")
        other_religion = request.POST.get("other_religion")
        ethnicity = request.POST.get("ethnicity")
        gravidity = request.POST.get("gravidity")
        parity = request.POST.get("parity")
        anc = request.POST.get("anc")
        total_anc_visits = request.POST.get("total_anc_visits")
        place_of_anc = request.POST.get("place_of_anc")
        gestational_age = request.POST.get("gestational_age")
        identified_risk_factors = request.POST.get("identified_risk_factors")
        other_risk_factors = request.POST.get("other_risk_factors")
        hiv_status = request.POST.get("hiv_status")
        on_ARV = request.POST.get("on_ARV")
        date_of_arrival = request.POST.get("date_of_arrival")
        time_of_arrival = request.POST.get("time_of_arrival")
        time_treatment_started = request.POST.get("time_treatment_started")
        referral_from_another_facility = request.POST.get("referral_from_another_facility")
        referral_from_where = request.POST.get("referral_from_where")
        time_to_reach_facility = request.POST.get("time_to_reach_facility")
        transport_type = request.POST.get("transport_type")
        other_transport_type = request.POST.get("other_transport_type")
        labour_occur = request.POST.get("labour_occur")
        labour_induced = request.POST.get("labour_induced")
        labour_augmented = request.POST.get("labour_augmented")
        photograph_used = request.POST.get("photograph_used")
        active_phase = request.POST.get("active_phase")
        second_stage = request.POST.get("second_stage")
        third_stage = request.POST.get("third_stage")
        patient_deliver = request.POST.get("patient_deliver")
        location_of_delivery = request.POST.get("location_of_delivery")
        other_location_of_delivery = request.POST.get("other_location_of_delivery")
        delivery_by = request.POST.get("delivery_by")
        delivery_by_others = request.POST.get("delivery_by_others")
        mode_of_delivery = request.POST.get("mode_of_delivery")
        delivery_outcome = request.POST.get("delivery_outcome")
        birth_weight = request.POST.get("birth_weight")
        days_since_termination = request.POST.get("days_since_termination")
        place_of_death = request.POST.get("place_of_death")
        other_place_of_death = request.POST.get("other_place_of_death")
        date_of_death = request.POST.get("date_of_death")
        time_of_death = request.POST.get("time_of_death")
        early_pregnancy = request.POST.get("early_pregnancy")
        antenatal = request.POST.get("antenatal")
        intrapartum = request.POST.get("intrapartum")
        postpartum = request.POST.get("postpartum")
        other_options = request.POST.get("other_options")
        other_interventions = request.POST.get("other_interventions")
        autopsy_performed = request.POST.get("autopsy_performed")
        date_autopsy_performed = request.POST.get("date_autopsy_performed")
        place_autopsy_performed = request.POST.get("place_autopsy_performed")
        autopsy_performed_by = request.POST.get("autopsy_performed_by")
        other_autopsy_performed_by = request.POST.get("other_autopsy_performed_by")
        final_COD = request.POST.get("final_COD")
        primary_obstetric_COD = request.POST.get("primary_obstetric_COD")
        other_primary_obstetric_COD = request.POST.get("other_primary_obstetric_COD")
        delay_in_seeking_help = request.POST.get("delay_in_seeking_help")
        specify_delay_in_seeking_help = request.POST.get("specify_delay_in_seeking_help")
        lack_of_transport_from_home = request.POST.get("lack_of_transport_from_home")
        specify_lack_of_transport_from_home = request.POST.get("specify_lack_of_transport_from_home")
        declined_treatment_admission = request.POST.get("declined_treatment_admission")
        specify_declined_treatment_admission = request.POST.get("specify_declined_treatment_admission")
        lack_of_transport_from_home_to_facility = request.POST.get("lack_of_transport_from_home_to_facility")
        specify_lack_of_transport_from_home_to_facility = request.POST.get("specify_lack_of_transport_from_home_to_facility")
        lack_of_transport_between_facility = request.POST.get("lack_of_transport_between_facility")
        specify_lack_of_transport_between_facility = request.POST.get("specify_lack_of_transport_between_facility")
        hf_communication_breakdown = request.POST.get("hf_communication_breakdown")
        specify_hf_communication_breakdown = request.POST.get("specify_hf_communication_breakdown")
        potential_avoidable_factors = request.POST.get("potential_avoidable_factors")
        lessons_learnt = request.POST.get("lessons_learnt")
        recommendations = request.POST.get("recommendations")
        isAudited = request.POST.get("isAudited") == 'on'
        names_of_team_members = request.POST.get("names_of_team_members")
        committee_chairman_name = request.POST.get("committee_chairman_name")
        committee_chairman_phone = request.POST.get("committee_chairman_phone")
        committee_chairman_rank = request.POST.get("committee_chairman_rank")
        forms_entered_by = request.POST.get("forms_entered_by")
        
        facility_region = Region.objects.get(id=facility_region_id)
        facility_district = District.objects.get(id=facility_district_id)
        facility_name = Facility.objects.get(id=facility_name_id)
        maternal_entry = MaternalEntry(
            facility_region=facility_region,
            facility_district=facility_district,
            facility_name=facility_name,
            name_of_deceased=name_of_deceased,
            dob_unknown=dob_unknown,
            date_of_birth=date_of_birth,
            age=age,
            educational_status=educational_status,
            occupation=occupation,
            other_occupation=other_occupation,
            marital_status=marital_status,
            religion=religion,
            other_religion=other_religion,
            ethnicity=ethnicity,
            gravidity=gravidity,
            parity=parity,
            anc=anc,
            total_anc_visits=total_anc_visits,
            place_of_anc=place_of_anc,
            gestational_age=gestational_age,
            identified_risk_factors=identified_risk_factors,
            other_risk_factors=other_risk_factors,
            hiv_status=hiv_status,
            on_ARV=on_ARV,
            date_of_arrival=date_of_arrival,
            time_of_arrival=time_of_arrival,
            time_treatment_started=time_treatment_started,
            referral_from_another_facility=referral_from_another_facility,
            referral_from_where=referral_from_where,
            time_to_reach_facility=time_to_reach_facility,
            transport_type=transport_type,
            other_transport_type=other_transport_type,
            labour_occur=labour_occur,
            labour_induced=labour_induced,
            labour_augmented=labour_augmented,
            photograph_used=photograph_used,
            active_phase=active_phase,
            second_stage=second_stage,
            third_stage=third_stage,
            patient_deliver=patient_deliver,
            location_of_delivery=location_of_delivery,
            other_location_of_delivery=other_location_of_delivery,
            delivery_by=delivery_by,
            delivery_by_others=delivery_by_others,
            mode_of_delivery=mode_of_delivery,
            delivery_outcome=delivery_outcome,
            birth_weight=birth_weight,
            days_since_termination=days_since_termination,
            place_of_death=place_of_death,
            other_place_of_death=other_place_of_death,
            date_of_death=date_of_death,
            time_of_death=time_of_death,
            early_pregnancy=early_pregnancy,
            antenatal=antenatal,
            intrapartum=intrapartum,
            postpartum=postpartum,
            other_options=other_options,
            other_interventions=other_interventions,
            autopsy_performed=autopsy_performed,
            date_autopsy_performed=date_autopsy_performed,
            place_autopsy_performed=place_autopsy_performed,
            autopsy_performed_by=autopsy_performed_by,
            other_autopsy_performed_by=other_autopsy_performed_by,
            final_COD=final_COD,
            primary_obstetric_COD=primary_obstetric_COD,
            other_primary_obstetric_COD=other_primary_obstetric_COD,
            delay_in_seeking_help=delay_in_seeking_help,
            specify_delay_in_seeking_help=specify_delay_in_seeking_help,
            lack_of_transport_from_home=lack_of_transport_from_home,
            specify_lack_of_transport_from_home=specify_lack_of_transport_from_home,
            declined_treatment_admission=declined_treatment_admission,
            specify_declined_treatment_admission=specify_declined_treatment_admission,
            lack_of_transport_from_home_to_facility=lack_of_transport_from_home_to_facility,
            specify_lack_of_transport_from_home_to_facility=specify_lack_of_transport_from_home_to_facility,
            lack_of_transport_between_facility=lack_of_transport_between_facility,
            specify_lack_of_transport_between_facility=specify_lack_of_transport_between_facility,
            hf_communication_breakdown=hf_communication_breakdown,
            specify_hf_communication_breakdown=specify_hf_communication_breakdown,
            potential_avoidable_factors=potential_avoidable_factors,
            lessons_learnt=lessons_learnt,
            recommendations=recommendations,
            isAudited=isAudited,
            names_of_team_members=names_of_team_members,
            committee_chairman_name=committee_chairman_name,
            committee_chairman_phone=committee_chairman_phone,
            committee_chairman_rank=committee_chairman_rank,
            forms_entered_by=forms_entered_by,
        )
        maternal_entry.save()
        messages.success(request, 'Maternal entry added successfully.')
        return redirect('add_new')    #redirect to index page
    
    return render(request, 'maternal_entry/add_new.html', context)




from django.http import JsonResponse

@login_required(login_url="authentication:my-login")
def get_districts_and_facilities(request):
    if request.method == 'GET' and 'region_id' in request.GET and 'district_id' in request.GET:
        region_id = request.GET.get('region_id')
        district_id = request.GET.get('district_id')

        # Fetch districts based on the selected region
        districts = District.objects.filter(district_region_id=region_id).values('id', 'district_name')

        # Fetch facilities based on the selected district if district_id is not empty
        if district_id:
            facilities = Facility.objects.filter(facility_district_id=district_id).values('id', 'facility_name')
        else:
            facilities = []

        return JsonResponse({'districts': list(districts), 'facilities': list(facilities)})
    else:
        return JsonResponse({'error': 'Invalid request'})

