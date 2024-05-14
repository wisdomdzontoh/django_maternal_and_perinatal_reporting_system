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