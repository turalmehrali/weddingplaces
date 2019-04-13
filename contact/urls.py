
from django.urls import path
from . import views

urlpatterns = [
    path('#contactpage/', views.contact, name='contact')
]