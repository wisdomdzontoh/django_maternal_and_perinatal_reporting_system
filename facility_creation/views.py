from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Region, District, Facility
from django.contrib.auth.models import User
from django.contrib import messages



@login_required(login_url="authentication:my-login")
def index(request):
    query = request.GET.get('q')
    regions = Region.objects.prefetch_related('district_set__facility_set').all()
    districts = District.objects.prefetch_related('facility_set').all()
    facilities = Facility.objects.all()
    
    if query:
        regions = regions.filter(region_name__icontains=query)
        districts = districts.filter(district_name__icontains=query)
        facilities = facilities.filter(facility_name__icontains=query)
    
    context = {
        'regions': regions,
        'districts': districts,
        'facilities': facilities,
        'query': query,
    }
    return render(request, 'facility_creation/index.html', context)





@login_required(login_url="authentication:my-login")
def add_region(request):
    regions = Region.objects.all()
    districts = District.objects.all()
    user = User.objects.all()
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

   
    return render(request, 'facility_creation/add_region.html', context)

    
            
        
        
        
        
    







