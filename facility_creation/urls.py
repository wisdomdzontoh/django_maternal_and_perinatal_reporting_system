from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    
    
    # Authentication URLs ------------------------------------------------#
    path('facility_creation', views.index, name="facility_creation"),  # Adjusted URL pattern
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
