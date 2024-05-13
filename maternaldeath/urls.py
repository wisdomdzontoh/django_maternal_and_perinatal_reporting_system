from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  # authentication urls for login and signup pages
    path('', include('facility_creation.urls')),  # facility_creation urls for login and signup pages
    path('', include('maternal_entry.urls')),  # maternal_entry urls 
    
    
    
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="authentication/reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
     path("__reload__/", include("django_browser_reload.urls")),
    
]
