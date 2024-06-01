from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='landing', permanent=False)),  # Redirect root URL to the register page
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include other app URLs
]
