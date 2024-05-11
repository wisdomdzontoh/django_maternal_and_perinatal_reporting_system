from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Region, District


@login_required(login_url="authentication:my-login")
def index(request):
    query = request.GET.get('q')
    regions = Region.objects.prefetch_related('district_set__facility_set').all()
    if query:
        regions = regions.filter(region_name__icontains=query)
    context = {
        'regions': regions,
        'query': query,
    }
    return render(request, 'facility_creation/index.html', context)






