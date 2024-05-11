from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Region, District, Facility
from django.contrib.auth.models import User



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
    user = User.objects.all()
    if request.method == 'POST':
        region_name = request.POST.get("region_name")
        region_code = request.POST.get("region_code")
        date_created = request.POST.get("date_created")
        created_by = request.POST.get("created_by")
        
        if region_name != "" and date_created:
            region = Region(
                region_name=region_name, 
                region_code=region_code,  
                date_created=date_created,
                created_by=created_by,
            )
            region.save()
            return render(request, 'facility_creation/add_region.html', { 'success': True })
        
    else:
        return render(request, 'facility_creation/add_region.html')
    return render(request, 'facility_creation/add_region.html')
            
        
        
        
        
    







