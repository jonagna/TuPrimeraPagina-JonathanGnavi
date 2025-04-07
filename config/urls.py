from django.contrib import admin
from django.urls import path, include
from autos import views as autos_views
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión finalizada con éxito.")
    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')),
    path('', autos_views.inicio, name='home'),

    
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('logout/', logout_view, name='logout'),
]
