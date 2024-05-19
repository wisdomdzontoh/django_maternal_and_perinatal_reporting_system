from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Region, District, Facility
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator



#view all on index page
@login_required(login_url="authentication:my-login")
def index(request):
    query = request.GET.get('q')
    regions = Region.objects.prefetch_related('district_set__facility_set').all()
    districts = District.objects.prefetch_related('facility_set').all()
    facilities = Facility.objects.all()

    total_facilities = Facility.objects.count()
    total_districts = District.objects.count()
    total_regions = Region.objects.count()
    
    if query:
        regions = regions.filter(region_name__icontains=query)
        districts = districts.filter(district_name__icontains=query)
        facilities = facilities.filter(facility_name__icontains=query)
    
    context = {
        'regions': regions,
        'districts': districts,
        'facilities': facilities,
        'query': query,
        "total_districts": total_districts,
        "total_facilities": total_facilities,
        "total_regions": total_regions,
    }
    return render(request, 'facility_creation/index.html', context)



#facility creation
@login_required(login_url="authentication:my-login")
def add_region(request):
    regions = Region.objects.all()
    districts = District.objects.all()
    context = {
        'regions': regions,
        'districts': districts,
    }
    
    
    if request.method == 'POST':
        if 'region_name' in request.POST and 'date_created' in request.POST:
            region_name = request.POST.get("region_name")
            region_code = request.POST.get("region_code")
            date_created = request.POST.get("date_created")
            created_by = request.POST.get("created_by")
            
            
            if region_name and date_created:
                region = Region(
                    region_name=region_name,
                    region_code=region_code,
                    date_created=date_created,
                    created_by=created_by,
                )
                region.save()
                messages.success(request, 'Region added successfully.')
                return redirect('add_region')  # Redirect to the same page after successful submission
        
        elif 'district_region' in request.POST and 'district_name' in request.POST:
            district_region_id = request.POST.get("district_region")
            district_name = request.POST.get("district_name")
            district_code = request.POST.get("district_code")
            date_created = request.POST.get("date_created")
            created_by = request.POST.get("created_by")
            
            
            if district_region_id and district_name:
                district_region = Region.objects.get(id=district_region_id)
                district = District(
                    district_region=district_region,
                    district_name=district_name,
                    district_code=district_code,
                    date_created=date_created,
                    created_by=created_by,
                )
                district.save()
                messages.success(request, 'District added successfully.')
                return redirect('add_region')  # Redirect to the same page after successful submission

        elif 'facility_region' in request.POST and 'facility_district' in request.POST and 'facility_name' in request.POST:
            facility_region_id = request.POST.get("facility_region")
            facility_district_id = request.POST.get("facility_district")
            facility_name = request.POST.get("facility_name")
            facility_code = request.POST.get("facility_code")
            date_created = request.POST.get("date_created")
            created_by = request.POST.get("created_by")
            
            
            if facility_region_id and facility_name and facility_district_id:
                facility_region = Region.objects.get(id=facility_region_id)
                facility_district = District.objects.get(id=facility_district_id)
                
                facility = Facility(
                    facility_region=facility_region,
                    facility_district=facility_district,
                    facility_name=facility_name,
                    facility_code=facility_code,
                    date_created=date_created,
                    created_by=created_by,
                )
                facility.save()
                messages.success(request, 'Facility added successfully.')
                return redirect('add_region')  # Redirect to the same page after successful submission
   
    return render(request, 'facility_creation/add_region.html', context)



#org unit cascade
@login_required(login_url="authentication:my-login")
def get_districts(request):
    if request.method == 'GET' and 'region_id' in request.GET:
        region_id = request.GET.get('region_id')
        districts = District.objects.filter(district_region_id=region_id).values('id', 'district_name')
        return JsonResponse({'districts': list(districts)})
    else:
        return JsonResponse({'error': 'Invalid request'})    



#view facility
@login_required(login_url="authentication:my-login")
def view_all_facility(request):
    facilities = Facility.objects.order_by('-facility_district').all()
    
    return render(request, 'facility_creation/view_facilities.html', {'facilities': facilities})




#Edit facility
@login_required(login_url="authentication:my-login")
def edit_facility(request, id):
    # Fetch the facility object to be edited
    facility = get_object_or_404(Facility, pk=id)
    
    # Fetch all regions and districts for dropdown options
    regions = Region.objects.all()
    districts = District.objects.all()
    
    context = {
        'facility': facility,
        'regions': regions,
        'districts': districts,
    }

    if request.method == 'POST':
        facility_region_id = request.POST.get("facility_region")
        facility_district_id = request.POST.get("facility_district")
        facility_name = request.POST.get("facility_name")
        facility_code = request.POST.get("facility_code")
        date_created = request.POST.get("date_created")
        created_by = request.POST.get("created_by")
        
        # Update the fields of the existing facility object
        facility.facility_region_id = facility_region_id
        facility.facility_district_id = facility_district_id
        facility.facility_name = facility_name
        facility.facility_code = facility_code
        facility.date_created = date_created
        facility.created_by = created_by
        
        facility.save()  # Save the changes
        messages.success(request, 'Facility updated successfully.')
          # Redirect to the same page after successful submission
    return render(request, 'facility_creation/edit_facility.html', context)





#delete facility
@login_required(login_url="authentication:my-login")
def delete_facility(request, id):
    if request.method == 'POST':
        facilities = Facility.objects.get(pk=id)
        facilities.delete()
        messages.success(request, 'Facility deleted successfully.')
        return redirect('view-all-facilities')          




# FILTER FOR FACILITY BASED ON DISTRICT OR FACILITY NAME
@login_required(login_url="authentication:my-login")
def filter_facility(request):
    # Get the filter parameters from the request
    facility_name = request.GET.get('facility_name')
    facility_district_name = request.GET.get('facility_district')

    # Filter facilities based on the provided parameters
    facilities = Facility.objects.all()
    if facility_name:
        facilities = facilities.filter(facility_name__icontains=facility_name)
    if facility_district_name:
        facilities = facilities.filter(facility_district__district_name__icontains=facility_district_name)

    # Render the template with the filtered facilities
    return render(request, 'facility_creation/view_facilities.html', {'facilities': facilities})


        
        
    







