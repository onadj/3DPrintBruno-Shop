from django.urls import path
from contact.views import contact_view
from django.views.generic import TemplateView

urlpatterns = [
    # Your existing URL patterns
    path('contact/', contact_view, name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact/contact_success.html'), name='contact_success'),
]