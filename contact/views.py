# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add code to send an email notification if needed
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
