from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout #authentication models views
from django.contrib.auth.decorators import login_required
from facility_creation.models import Region, District, Facility
from maternal_entry.models import MaternalEntry

# Create your views here.
def homepage(request):
    
    return render(request, 'authentication/index.html')

def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":  # If the form has been submitted...
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'registerform':  form}
    
    return render(request, 'authentication/register.html', context=context)

def my_login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect("dashboard")
    
    context = {'loginform': form }
    
    return render(request, 'authentication/my-login.html', context=context)

def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")



@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'authentication/dashboard.html')



@login_required(login_url="my-login")
def dashboard(request):
    regions = Region.objects.all()
    districts = District.objects.all()
    facilities = Facility.objects.all()
    total_facilities = Facility.objects.count()
    total_districts = District.objects.count()
    total_regions = Region.objects.count()
    total_maternal_deaths = MaternalEntry.objects.count()
    total_audited = MaternalEntry.objects.filter(isAudited=True).count()
    total_unaudited = total_maternal_deaths - total_audited
    # Calculate the percentage audited rounded to 2 decimal places
    percent_audited = round((total_audited / total_maternal_deaths) * 100, 2)
    entries = MaternalEntry.objects.all()[:3]
    
    
    context = {
        "total_districts": total_districts,
        "total_facilities": total_facilities,
        "total_regions": total_regions,
        "regions": regions,
        "districts": districts,
        "facilities": facilities,
        "total_maternal_deaths": total_maternal_deaths,
        "percent_audited": percent_audited,
        "entries": entries,
        "total_unaudited": total_unaudited,
        
    }
    return render(request, 'authentication/dashboard.html', context)
