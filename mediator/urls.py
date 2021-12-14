from django.urls import path
from mediator import views

urlpatterns = [
    path("", views.mediator, name="mediator"),
    path("medlogin", views.medlogin, name='medlogin'),
    path("logout", views.logout, name='logout'),
    path("contacts", views.allcontact, name="allcontact"),
    path("service_providers", views.service_providers, name="service_providers"),
    path("change_status", views.contact_status, name="contact_status"),
    path("change_status_service", views.service_status, name="service_status"),
    path("reset", views.reset, name="reset")
]