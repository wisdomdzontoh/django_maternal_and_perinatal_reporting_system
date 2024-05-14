from django.urls import path
from authentication import views as auth_views  # Correct import statement
from . import views


urlpatterns = [
    
    path('maternal_entry/add_new', views.add_new, name="add_new"),  # Adjusted URL pattern
    path('maternal_entry', views.index, name="maternal_entry"),  # Adjusted URL pattern
    
    # Authentication URLs ------------------------------------------------#
    path('authentication/user-logout/', auth_views.user_logout, name="user-logout"),  # Corrected import path and removed unnecessary comment
]
