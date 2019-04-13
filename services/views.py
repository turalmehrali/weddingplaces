
from django.shortcuts import render
from .models import Services

# Create your views here.

def services(request):
    services_list = Services.objects.all()
    return render(request, 'services.html', {'services': services_list})