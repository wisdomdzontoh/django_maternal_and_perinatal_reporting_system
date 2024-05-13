from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views
from .views import get_districts


urlpatterns = [
    path('add_region', views.add_region, name="add_region"),
    path('get_districts/', views.get_districts, name='get_districts'),
    path('view-all-facilities/', views.view_all_facility, name='view-all-facilities'),
    path('facilities/<int:id>/delete/', views.delete_facility, name='facilities/delete'),
    path('filter-facility/', views.filter_facility, name='filter-facility'),
    path('facility/edit/<int:id>/', views.edit_facility, name='edit-facility'),
    
    path('facility_creation', views.index, name="facility_creation"),  # Adjusted URL pattern
    
    
    
    
    
    # Authentication URLs ------------------------------------------------#
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
