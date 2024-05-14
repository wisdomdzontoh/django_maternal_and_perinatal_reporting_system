from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from facility_creation.models import Region, District, Facility


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

