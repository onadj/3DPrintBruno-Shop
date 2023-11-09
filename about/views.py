from django.shortcuts import render
from .models import About

def about_us(request):
    about = About.objects.first()  # Retrieve the first About object; you can modify this logic based on your needs
    return render(request, 'about/about_us.html', {'about': about})
