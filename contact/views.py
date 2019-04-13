
from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name_form = request.POST.get('name')
        email_form = request.POST.get('email')
        message_form = request.POST.get('message')

        contact_form = Contact(name=name_form, email=email_form, message=message_form)
        contact_form.save()

        return redirect('homepage')

    else:
        return render(request, 'homepage.html')